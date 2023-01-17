from tabulate import tabulate
from money import Money


class Transaction:
    '''
    '''

    def __init__(self):
        self.item = {'Nama Item': [], 'Jumlah': [], 'Harga per Item': [],
                     "Harga": []}

    def add_item(self):
        '''
        Adding an item into the order list.
        Params: None
        Inputs:\n 
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

            print('**Pesanan berhasil ditambahkan!**')
        except ValueError:
            print("Data yang Anda masukkan tidak valid.")
            self.add_item()

    def update_item_name(self):
        '''
        Updating an existing item name in the order list.
        Params: None
        Inputs:\n
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
        else:
            print('Data yang Anda maksud tidak tersedia')
            Transaction.update_item_name(self)
            self.update_item_name()

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

        if nama_item in self.item['Nama Item']:
            idx = self.item['Nama Item'].index(nama_item)
            self.item['Harga per Item'][idx] = harga_per_item_updated
            self.item['Harga'][idx] = harga_per_item_updated * \
                self.item['Jumlah'][idx]
        else:
            print("Data yang Anda maksud tidak tersedia")

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

            removed_element = [data[idx] for data in self.item.values()]
            headers = [header for header in self.item.keys()]
            print(tabulate(removed_element, headers=headers, tablefmt='github'))

            answer = input("Data berikut akan dihapus. Lanjutkan? Y/N\n")
            if answer in ('Y', 'y'):
                for data in self.item.values():
                    data.pop(idx)

    def reset_transaction(self):
        '''
        Delete all existing item in the order list.
        Return: None
        '''
        ans = input("Seluruh transaksi akan dihapus. Lanjutkan? Y/N\n")
        if ans in ('Y', 'y'):
            for data in self.item.values():
                del data[:]

            print("Semua transaksi telah dihapus")
            print(tabulate(self.item, headers='keys', tablefmt='github'))

    def total_price(self):
        '''
        Displaying total price.
        Return: None
        '''
        total = sum(self.item['Harga'])

        if total > 400_000:
            total = total * (1 - 0.1)
        elif total > 300_000:
            total = total * (1 - 0.08)
        elif total > 200_000:
            total = total * (1 - 0.05)

        print(f"Harga total: {total}")

    def check_order(self):
        # TODO: gimana cara implementasi fungsi ini
        '''
        <enaknya diisi apa ya?>
        '''
        try:
            total_jml_item = sum(self.item['Jumlah'])
            total_harga = sum(self.item['Harga'])

            print(tabulate(self.item, headers='keys', tablefmt="github"))
            print(f"Total jumlah item: {total_jml_item}")
            print(f"Total harga: {total_harga}")
            print("Data yang Anda masukkan sudah benar")

        except Exception as exc:
            raise ValueError("Terdapat kesalahan input data") from exc
