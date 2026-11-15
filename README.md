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
