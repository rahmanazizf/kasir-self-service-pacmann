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

            

tsx_123 = Transaction()

tsx_123.add_item('Roti', 1, 7000)
tsx_123.update_item_name('Roti', 'Sari Roti')
print(tsx_123.item)

