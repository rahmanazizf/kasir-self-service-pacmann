from transaction import Transaction

tsx123 = Transaction()
cmd_trx = {1: tsx123.add_item,
           2: tsx123.update_item_name,
           3: tsx123.update_item_price,
           4: tsx123.delete_item,
           5: tsx123.reset_transaction,
           6: tsx123.check_order,
           7: tsx123.total_price,
           8: quit}

print("="*28)
print('Self-Service Pac-Cashier')
print("="*28)

def menu():
    '''
    Performing a particular action entered by user.
    Parameters: None
    Input: Choice of action to perform (int)
    Return: None
    '''
    # print("="*28)
    print("Silakan ketikkan angka pada menu berikut.")
    print('''
    1. Tambahkan item belanja
    2. Ubah nama item terdaftar
    3. Ubah harga item terdaftar
    4. Hapus item terdaftar
    5. Hapus seluruh transaksi
    6. Cek pesanan
    7. Harga total
    8. Keluar\n
    ''')

    try:
        cmd_number = int(input("Perintah Anda: "))
    except ValueError:
        # jika perintah yang dimasukkan bukan integer maka tampilkan pesan dan kembali ke menu
        print("Perintah yang Anda masukkan tidak valid")
        menu()

    cmd_trx[cmd_number]()

    # panggil menu terus menerus sampai user menginput nomor 8
    menu()


menu()
