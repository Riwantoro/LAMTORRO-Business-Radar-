# LAMTORRO Business Radar

Aplikasi prospek bisnis untuk MacBook. Pencarian Bali menggunakan batas administratif seluruh provinsi. Mode Global menerima nama kota dan negara.

## Jalankan di MacBook

Dengan Node.js 22 atau lebih baru:

```sh
git clone https://github.com/Riwantoro/LAMTORRO-Business-Radar-.git
cd LAMTORRO-Business-Radar-
node server.mjs
```

Buka http://127.0.0.1:4173. Pilih **Data contoh** untuk mencoba tanpa internet. Pencarian langsung membutuhkan koneksi ke OSM.

## Alur kerja

1. Pilih wilayah dan industri. Utamakan bisnis yang sumbernya belum mencantumkan situs.
2. Buka sumber OpenStreetMap, Google Search, dan Google Maps untuk memeriksa situs resmi, kontak, dan ulasan.
3. Simpan prospek, catatan, tahap, dan situs resmi yang sudah diperiksa. CRM disimpan di browser untuk alamat lokal yang digunakan.
4. Unduh demo HTML yang memakai nama, kategori, lokasi, serta tautan kontak yang tersedia. Tinjau demo sebelum menawarkannya.
5. Ambil tautan ulasan resmi dari Google Business Profile. Buat QR lewat QuickChart dan gunakan tautan yang sama ketika menulis tag NFC. Berikan undangan netral kepada semua pelanggan untuk menulis ulasan jujur.

## Skor dan cakupan

Skor menjumlahkan status situs (0–55), kontak langsung (25), alamat (10), dan profil publik (10). Data OSM yang kosong perlu diperiksa sebelum menyimpulkan bahwa situs atau kontak tidak tersedia. Pencarian dibatasi hingga 1.200 entri per industri dan wilayah. Kelengkapan situs dan kontak bergantung pada pemetaan OpenStreetMap. Mode Global bergantung pada tersedianya batas administratif kota di Nominatim dan Overpass.

Versi awal memakai HTML, CSS, dan JavaScript tanpa dependensi. Astryx, Scrapling, audit otomatis ulasan dan foto, hosting demo, dan sinkronisasi CRM belum terintegrasi. Repositori berisi kode dan data contoh fiktif. Data CRM tersimpan di browser.

## Pencarian Bali saat Overpass gagal

Buat berkas data satu kali dengan Python 3 dan ekstrak OpenStreetMap. Unduhan Geofabrik berukuran sekitar 168 MB.

```sh
python3 -m venv .radar-venv
.radar-venv/bin/python -m pip install 'osmium>=4,<5'
curl -fL https://download.geofabrik.de/asia/indonesia/nusa-tenggara-latest.osm.pbf -o /tmp/nusa-tenggara.osm.pbf
.radar-venv/bin/python build_bali_snapshot.py /tmp/nusa-tenggara.osm.pbf --output /tmp/bali-businesses.json
```

Di aplikasi, pilih **Seluruh Bali**, pilih berkas `/tmp/bali-businesses.json` di **Data Bali offline**, pilih industri, lalu klik **Cari bisnis**. Aplikasi membaca berkas di browser dan pencarian ini tidak menghubungi Overpass. Gunakan ekstrak yang sudah dipotong sesuai batas Bali bila perlu ketepatan administratif. Pembuat berkas memakai kotak koordinat sekitar Bali dan hanya menyertakan titik serta bangunan dengan kategori dan nama yang sesuai. Cakupan mengikuti ekstrak sumber. Data © kontributor OpenStreetMap, tersedia menurut ODbL.
