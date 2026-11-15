"""Build an offline Bali business snapshot from a Geofabrik PBF extract."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import osmium

TAGS = {
    "amenity": {"cafe", "restaurant", "fast_food", "clinic", "dentist", "doctors"},
    "tourism": {"hotel", "guest_house", "villa", "resort", "apartment"},
    "shop": {"beauty", "hairdresser", "massage", "clothes", "gift", "convenience",
             "supermarket", "car_repair", "motorcycle_repair", "tyres", "laundry", "dry_cleaning"},
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("extract", type=Path)
    parser.add_argument("--output", type=Path, default=Path("bali-businesses.json"))
    args = parser.parse_args()
    elements = []
    for item in osmium.FileProcessor(str(args.extract)).with_locations("sparse_file_array"):
        if not item.is_node() and not item.is_way():
            continue
        tags = item.tags
        if not tags.get("name") or not any(tags.get(key) in values for key, values in TAGS.items()):
            continue
        if item.is_node():
            if not item.location.valid():
                continue
            lat, lon = item.location.lat, item.location.lon
        else:
            points = [(node.lat, node.lon) for node in item.nodes if node.location.valid()]
            if not points:
                continue
            lat = sum(point[0] for point in points) / len(points)
            lon = sum(point[1] for point in points) / len(points)
        # The extract should be clipped to Bali before import for exact boundaries.
        if not (-9.0 <= lat <= -8.0 and 114.4 <= lon <= 115.75):
            continue
        public_tags = {tag.k: tag.v for tag in tags if tag.k in
                       {"name", "amenity", "shop", "tourism", "website", "url",
                        "phone", "email", "whatsapp", "facebook", "instagram"}
                       or tag.k.startswith(("contact:", "addr:"))}
        elements.append({"type": "node" if item.is_node() else "way", "id": item.id,
                         "lat": lat, "lon": lon, "tags": public_tags})
    if not elements:
        raise SystemExit("Tidak ada bisnis Bali yang ditemukan dalam ekstrak ini.")
    data = {"elements": elements, "generatedAt": datetime.now(timezone.utc).isoformat()}
    temporary = args.output.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    temporary.replace(args.output)
    print(f"{len(elements):,} bisnis ditulis ke {args.output}")


if __name__ == "__main__":
    main()
