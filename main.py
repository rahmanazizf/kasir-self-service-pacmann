from tabulate import tabulate
import numpy as np
from transaction import Transaction

tsx123 = Transaction()

print("=== Self-Service Cashier ===")
print("Selamat datang di Self-Service Cashier")

def menu():
    print("Silakan ketikkan angka pada menu berikut\n")
    print('''
    1. Tambahkan item belanja
    2. Ubah nama item terdaftar
    3. Ubah harga item terdaftar
    4. Hapus item terdaftar
    5. Hapus seluruh transaksi
    6. Cek pesanan
    7. Harga total
    ''')
    cmd_number = int(input("Perintah Anda: "))

    return cmd_number

cmd_trx = {1: tsx123.add_item, 2: tsx123.update_item_name, 3: tsx123.update_item_price}

