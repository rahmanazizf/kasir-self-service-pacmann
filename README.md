# Self-Service Cashier Pacmann
# Latar Belakang
Untuk melakukan perbaikan proses bisnis, siswa diminta untuk membuat sistem kasir yang dapat digunakan untuk pelayanan mandiri oleh pelanggan.
# Tujuan
Membuat sistem kasir sederhana dengan yang dapat mengeksekusi tugas-tugas sebagai berikut.
  - menambahkan barang yang akan dibeli
  - memperbarui nama, jumlah, atau harga dari barang yang akan dibeli
  - menghapus salah satu atau semua barang yang terdapat dalam daftar belanja
  - mengecek kembali daftar belanja yang telah dimasukkan
# Requirements
Paket-paket yang diperlukan untuk menjalankan program sudah disertakan dalam file req.txt. Pengguna hanya perlu mengetikkan perintah berikut pada terminal:
```
python -m pip install -r req.txt
```
lalu jalankan program dengan perintah 
```
python main.py
```
# Penjelasan Singkat
Di dalam class Transaction terdapat beberapa fungsi yang dapat menjalankan tugas-tugas spesifik.
1. **Fungsi add_item**
  Fungsi ```add_item``` menambahkan item yang diinput oleh user ke dalam daftar pesanan. Fungsi ini dijalankan dengan memasukkan pilihan menu nomor 1 pada tampilan utama.
  
      ![2023-01-21 (1)](https://user-images.githubusercontent.com/100136072/213847715-e7791995-d311-4e33-a7aa-b5c0a2ed9d1f.png "Fungsi add_item")
