from tabulate import tabulate
from money import Money
from decimal import Decimal
import sys


class Transaction:
    '''
    Class containing methods to process a transaction.
    '''
    def __init__(self):
        self.item = {'Nama Item': [], 'Jumlah': [], 'Harga per Item': [],
                     "Harga": []}

    def add_item(self):
        '''
        Adding an item into the order list.
        Params: None
        Inputs:
            Item name (str)
            Number of item to buy (int)
            Price per item (Money)
        Return: None
        '''
        try:
            print(30*'*')
            print("Menambahkan item belanja")
            nama_item = input("Masukkan nama item belanja: ")
            jumlah_item = int(input("Masukkan jumlah item: "))
            harga_per_item = Money(input("Harga per item: "), 'IDR')

            self.item['Nama Item'].append(nama_item)
            self.item['Jumlah'].append(jumlah_item)
            self.item['Harga per Item'].append(harga_per_item)
            self.item['Harga'].append(harga_per_item * jumlah_item)

            print('***Pesanan berhasil ditambahkan!***')
        except ValueError:
            print("Data yang Anda masukkan tidak valid.")

    def update_item_name(self):
        '''
        Updating an existing item name in the order list.
        Params: None
        Inputs:
            Existing item name (str)
            New item name (str)
        Return: None
        '''
        print("Mengubah nama item belanja")

        nama_item = input("Masukkan nama yang telah terdaftar sebelumnya: ")
        nama_item_updated = input("Masukkan nama item baru: ")

        if nama_item in self.item['Nama Item']:
            idx = self.item['Nama Item'].index(nama_item)
            self.item['Nama Item'][idx] = nama_item_updated
            print("*** Nama item telah diperbarui! ***")
        else:
            print('!!! Item yang Anda maksud tidak tersedia !!!')

    def update_item_price(self):
        '''
        Updating an existing item price in the order list.
        Params: None
        Inputs:
            Item name (str)
            Price per item updated (Money)
        Return: None
        '''
        print("Mengubah harga item belanja")

        nama_item = input("Masukkan nama item: ")
        harga_per_item_updated = Money(
            input("Masukkan harga item baru: "), 'IDR')

        try:
            if nama_item in self.item['Nama Item']:
                idx = self.item['Nama Item'].index(nama_item)
                self.item['Jumlah'][idx] = harga_per_item_updated
                self.item['Harga'][idx] = harga_per_item_updated * \
                self.item['Jumlah'][idx]
                print("*** Harga item telah diperbarui! ***")
            else:
                print("!!! Item yang Anda maksud tidak tersedia !!!")
                print(30*'=')
        
        except TypeError:
            # handle kasus jika variable nama_item berisi empty string
            print("!!! Terdapat kesalahan dalam input data !!!")
            print(30*'=')
        
        finally:
            self.update_item_price()


    def update_item_qty(self):
        '''
        Updating an existing item quantity in the order list.
        Params: None
        Inputs:
            Item name (str)
            Item quantity updated (int)
        Return: None
        '''
        print("Mengubah jumlah item")

        nama_item = input("Masukkan nama item: ")
        jumlah_item_updated = int(input("Masukkan jumlah item baru: "))

        try:
            if nama_item in self.item['Nama Item']:
                idx = self.item['Nama Item'].index(nama_item)
                self.item['Jumlah'][idx] = jumlah_item_updated
                self.item['Harga'][idx] = jumlah_item_updated * \
                self.item['Harga per Item'][idx]
                print("*** Jumlah item telah diperbarui! ***")
            else:
                print("!!! Item yang Anda maksud tidak tersedia !!!")
                print(30*'=')
        
        except TypeError:
            # handle kasus jika variable nama_item berisi empty string
            print("!!! Terdapat kesalahan dalam input data !!!")
            print(30*'=')
        
        finally:
            self.update_item_price()

    def delete_item(self):
        '''
        Deleting an existing item in the order list.
        Params: None
        Inputs:
            Item name (str)
        Return: None
        '''
        print("Manghapus item belanja")

        nama_item = input("Masukkan nama item: ")

        if nama_item in self.item['Nama Item']:
            idx = self.item['Nama Item'].index(nama_item)

            removed_element = [[data[idx] for data in self.item.values()]]
            headers = list(self.item)
            print(tabulate(removed_element, headers=headers, tablefmt='github'))

            answer = input("Data tersebut akan dihapus. Lanjutkan? Y/N\n")
            if answer in ('Y', 'y'):
                for data in self.item.values():
                    data.pop(idx)

                print(f'*** Item {nama_item} berhasil dihapus! ***')

    def reset_transaction(self):
        '''
        Delete all existing item in the order list.
        Return: None
        '''
        ans = input("Seluruh transaksi akan dihapus. Lanjutkan? Y/N\n")
        if ans in ('Y', 'y'):
            for data in self.item.values():
                del data[:]

            print("*** Semua transaksi telah dihapus ***")
            print(tabulate(self.item, headers='keys', tablefmt='github'))

    def total_price(self):
        '''
        Displaying total price.
        Return: None
        '''
        total = sum(self.item['Harga'])
        prc_discs = ((400000, 0.1), (300000, 0.08), (200000, 0.05))
        
        for prc in prc_discs:
            disc = prc[1] if total > Money(prc[0], 'IDR') else 0.0
            if disc: 
                break

        total_disc = total * Decimal(1 - disc)

        print(f'''
        ========================= 
        Harga total: {total_disc} 
        =========================''')

    def check_order(self):
        '''
        Checking if there is empty string in item name and 
        displaying existing items in order list.
        Return: None
        '''
        try:
            assert('' not in self.item['Nama Item'])
            print(tabulate(self.item, headers='keys', tablefmt="github"))
            print("Data yang Anda masukkan sudah benar")

        except AssertionError:
            print("!!! Nama item tidak boleh kosong !!!")
    
    def exit(self):
        '''
        Exiting the program
        '''
        sys.exit()
