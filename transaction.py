from tabulate import tabulate

class Transaction:

    def __init__(self):
        self.item = {'Nama Item': [], 'Jumlah': [], 'Harga per Item': []}

    def add_item(self):
        try:
            print("Menambahkan item belanja")
            nama_item = input("Masukkan nama item belanja: ")
            jumlah_item = int(input("Masukkan jumlah item: "))
            harga_per_item = float(input("Harga per item: "))

            self.item['Nama Item'].append(nama_item)
            self.item['Jumlah'].append(jumlah_item)
            self.item['Harga per Item'].append(harga_per_item)

        except Exception as exc:
            raise ValueError("Data yang Anda masukkan tidak valid") from exc
        
    def update_item_name(self):
        print("Mengubah nama item belanja")

        nama_item = input("Masukkan nama yang telah terdaftar sebelumnya: ")
        nama_item_updated = input("Masukkan nama item baru: ")

        if nama_item in self.item['Nama Item']:
            idx = self.item['Nama Item'].index(nama_item)
            self.item['Nama Item'][idx] = nama_item_updated
        else:
            print('Data yang Anda maksud tidak tersedia')


    def update_item_price(self):
        print("Mengubah harga item belanja")

        nama_item = input("Masukkan nama item: ")
        harga_per_item_updated = float(input("Masukkan harga item baru: "))

        if nama_item in self.item['Nama Item']:
            idx = self['Nama Item'].index(nama_item)
            self.item['Harga per Item'][idx] = harga_per_item_updated
        else:
            print("Data yang Anda maksud tidak tersedia")

    def delete_item(self):
        print("Manghapus item belanja")

        nama_item = input("Masukkan nama item: ")

        if nama_item in self.item['Nama Item']:
            idx = self.item['Nama Item'].index(nama_item)

            removed_element = []
            for data in self.item.values():
                removed_element.append(data.pop(idx))
            
            print("Data berikut telah berhasil dihapus.")
            print(removed_element)

    def reset_transaction(self):
        print("Menghapus seluruh transaksi belanja")
        self.item.clear()
        print("Semua transaksi telah dihapus")


    def check_order(self):
        pass

    def total_price(self):
        total = 0

        for n_item, price in zip(self.item['Jumlah'], self.item['Harga per Item']):
            total += n_item * price
        
        if total > 400_000:
            total = total * (1 - 0.1)
        elif total > 300_000:
            total = total * (1 - 0.08)
        elif total > 200_000:
            total = total * (1 - 0.05)
        
        print(f"Harga total: {total}")
                    

# tsx_123 = Transaction()

# tsx_123.add_item('Roti', 1, 7000)
# tsx_123.update_item_name('Roti', 'Sari Roti')
# print(tsx_123.item)

