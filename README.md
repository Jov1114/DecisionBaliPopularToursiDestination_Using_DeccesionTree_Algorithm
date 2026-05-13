# Bali Tourist Destination Decision Tree

Project sederhana untuk menentukan destinasi wisata di Bali menggunakan algoritma Decision Tree. Aplikasi ini menggunakan data destinasi tahun 2022 dan memberikan rekomendasi berdasarkan rating, jumlah ulasan, dan biaya (USD).

<p align="center">
  <img src="https://github.com/Jov1114/Decision-Popular-Tourist-Destination-in-bali-using-DecessionTree-Algorithm/assets/108922816/2cd86e62-93cc-4243-820d-e74972b74e03" width="500">
</p>

## Cara Kerja
Aplikasi menggunakan `DecisionTreeClassifier` dari library `scikit-learn` untuk mempelajari pola dari dataset `Bali Popular Destination for Tourist 2022`. User cukup memasukkan kriteria yang diinginkan, dan aplikasi akan menampilkan tempat yang paling cocok.

## Persiapan
Pastikan sudah install Python 3, lalu install library yang dibutuhkan:
```bash
pip install -r requirements.txt
```

## Cara Pakai
Cukup jalankan file `visual.py`:
```bash
python visual.py
```
Masukkan nilai rating (0-5), jumlah ulasan, dan budget dalam USD pada kolom yang tersedia.

## Dataset
Dataset diambil dari file CSV yang berisi:
- Nama & Lokasi tempat wisata
- Koordinat Google Maps
- Rating & Jumlah Ulasan
- Deskripsi singkat & Estimasi biaya kunjungan

## Tech Stack
- Python (Tkinter untuk GUI)
- Scikit-Learn (Decision Tree)
- CSV (Data Storage)
