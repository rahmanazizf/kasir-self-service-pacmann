from tabulate import tabulate
import numpy as np

class Transaction:

    def __init__(self):
        self.nama_item = []
        self.jumlah_item = []
        self.harga_per_item = []

    def add_item(self):
        nama_item = input("Masukkan nama item: ")
        jumlah_item = input("Masukkan jumlah item: ")
        harga_per_item = input("Masukkan harga per item: ")

        try:
            self.nama_item = str(nama_item)

            if int(jumlah_item) | int(harga_per_item) > 0:
                self.jumlah_item.append(int(jumlah_item))
                self.harga_per_item.append(int(harga_per_item))
            else:
                raise ValueError("Jumlah item/harga per item harus lebih dari 0")

        except:
            raise TypeError("Data yang Anda Masukkan tidak valid.")
    
    def hitung_harga_total(self):
        try:
            return self.jumlah_item * self.harga_per_item
        except:
            raise ValueError("Item yang Anda maksud tidak terdaftar")
            
        


tsc12 = Transaction()
tsc12.add_item()

# print(tsc12.harga_per_item)
# print(tsc12.nama_item)