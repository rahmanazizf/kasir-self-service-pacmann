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
 1. Fungsi ```add_item()``` menambahkan item yang diinput oleh user ke dalam daftar pesanan. Fungsi ini dijalankan dengan memasukkan pilihan menu nomor 1 pada tampilan utama. Input yang diminta oleh program adalah nama item, jumlah item, dan harga item.
      
 2. Fungsi ```update_item_name()``` memperbarui nama item yang sudah terdaftar di dalam pesanan. Input yang diminta adalah nama item yang ingin diperbarui dan nama item baru.
   
 3. Fungsi ```update_item_price()``` memperbarui harga item yang telah terdaftar. Input yang diminta adalah nama item dan harga item baru.
 
 4. Fungsi ```update_item_qty()``` memperbarui jumlah item tertentu yang telah terdaftar. Input yang diminta adalah nama item dan jumlah item baru.
 
 5. Fungsi ```delete_item()``` menghapus satu item dari daftar. Input yang diminta adalah nama item.
   
 6. Fungsi ```reset_transaction()``` menghapus seluruh item yang telah terdaftar.
 
 7. Fungsi ```check_order()``` memeriksa seluruh item di daftar pesanan dan memastikan tidak ada item yang namanya tidak tercantum.
 
 8. Fungsi ```total_price()``` menghitung total harga dari seluruh item dalam daftar pesanan.

# Diagram Alir Cara Kerja Program
![image](https://user-images.githubusercontent.com/100136072/213872770-11194034-b2aa-4ae0-9ae5-3c89a09ad2f7.png "Diagram alir cara kerja program")

# Test Cases
## 1. Menambahkan pesanan dengan fungsi add_item()
Item yang ditambahkan: Ayam Goreng (2) dengan harga Rp 20.000 dan Pasta Gigi (2) dengan harga Rp 15.000

![image](https://user-images.githubusercontent.com/100136072/213850964-deb51a5f-afba-46f0-a80e-30a1581e8f19.png "Menambahkan item Ayam Goreng")

![image](https://user-images.githubusercontent.com/100136072/213851448-9254b9c1-e7d9-47fd-8567-98a1e53875d6.png "Menambahkan item Pasta Gigi")

Tampilkan daftar pesanan

![image](https://user-images.githubusercontent.com/100136072/213851842-0ce26c02-1e93-4a1e-b2bd-54a6cd577753.png "Menampilkan pesanan")
## 2. Menghapus pesanan dengan fungsi delete_item()
Item yang dihapus: Pasta Gigi

![image](https://user-images.githubusercontent.com/100136072/213852824-0445480b-0128-4660-964d-093e9e975268.png "Menghapus item Pasta Gigi")

Cek kembali seluruh pesanan

![image](https://user-images.githubusercontent.com/100136072/213853293-8ff9718e-97ea-450b-89ee-cf5c1207899b.png "Cek daftar pesanan")

## 3. Menghapus seluruh pesanan dengan fungsi reset_transaction()
![image](https://user-images.githubusercontent.com/100136072/213861228-7893121a-03b5-4240-b566-8654f5f4aca8.png "Menghapus seluruh transaksi")

## 4. Menghitung total harga seluruh item dengan fungsi total_price()
Pesanan yang telah terdaftar

![image](https://user-images.githubusercontent.com/100136072/213861356-3e0af6d8-7b08-4be1-978c-9dad0289ed0a.png "Menghitung total harga seluruh item")

Total harga yang harus dibayar

![image](https://user-images.githubusercontent.com/100136072/213861863-cf720dd9-5ee1-4e1d-b447-dfc8ef869423.png "Harga total")

# Saran Perbaikan
- membuat program terkoneksi dengan database
- menggunakan framework Object Relational Mapping seperti ```sqlalchemy``` untuk pembuatan objek
