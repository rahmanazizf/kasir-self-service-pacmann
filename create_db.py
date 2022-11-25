import mysql.connector
from mysql.connector import Error
import init_variables

# definisikan variabel nama host, user, password, dan nama database
host = init_variables.host
user = init_variables.user
pwd = init_variables.password
db_name = init_variables.dbname

# menyambungkan modul python dengan server
conn = mysql.connector.connect(
    host,
    user,
    pwd,
    db_name
)

# instantiate objek cursor
cr = conn.cursor()

def create_db():

# try
# create database dengan query sql
    try:
        # menyimpan query dalam variable
        sql_create_db = "CREATE DATABASE IF NOT EXISTS {}".format(db_name)
        # mengeksekusi pembuatan database
        cr.execute(sql_create_db)
# except
# jika database telah dibuat sebelumnya, maka pesan di bawah akan muncul
    except:
        print("Database sudah tersedia. Jalankan program main.py")
        print("="*40)

# membuat tabel dalam database
# fungsi yang mengeksekusi values dalam dictionary yang terdiri
# dari query sql untuk membuat beberapa tabel
def create_table():
    



# membuat fungsi untuk memasukkan data ke dalam tabel (opsional)