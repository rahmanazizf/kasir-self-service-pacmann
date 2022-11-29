from tabulate import tabulate

class Transaction:

    def __init__(self):
        self.item = {'Nama Item': [], 'Jumlah': [], 'Harga per Item': []}

    def add_item(self, nama_item, jumlah_item, harga_per_item):
        try:
            harga_per_item = float(harga_per_item)

            if (type(nama_item) == str) & (type(jumlah_item) == int) & (type(harga_per_item) == float):
                self.item['Nama Item'].append(nama_item)
                self.item['Jumlah'].append(jumlah_item)
                self.item['Harga per Item'].append(harga_per_item)

        except Exception as exc:
            raise ValueError("Data yang Anda masukkan tidak valid") from exc
        
    def update_item_name(self, nama_item, nama_item_updated):
        
        if nama_item in self.item['Nama Item']:
            idx = self.item['Nama Item'].index(nama_item)
            self.item['Nama Item'][idx] = nama_item_updated
        else:
            print('Data yang Anda maksud tidak tersedia')


    def update_item_price(self, nama_item, harga_per_item_updated):
        if nama_item in self.item['Nama Item']:
            idx = self['Nama Item'].index(nama_item)
            self.item['Harga per Item'][idx] = harga_per_item_updated
        else:
            print("Data yang Anda maksud tidak tersedia")

    def delete_item(self, nama_item):
        if nama_item in self.item['Nama Item']:
            idx = self.item['Nama Item'].index(nama_item)

            removed_element = []
            for data in self.item.values():
                removed_element.append(data.pop(idx))
            
            print("Data berikut telah berhasil dihapus.")
            print(removed_element)

    def reset_transaction(self):
        self.item.clear()
        print("Semua transaksi telah dihapus.")


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
                    

tsx_123 = Transaction()

tsx_123.add_item('Roti', 1, 7000)
tsx_123.update_item_name('Roti', 'Sari Roti')
print(tsx_123.item)

