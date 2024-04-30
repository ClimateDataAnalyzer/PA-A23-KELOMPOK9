# PROJECT AKHIR A`23 KELOMPOK 9
## Program SDGs Climate Action (CLIMATE DATA ANALYZER)

### A. DESKRIPSI PROGRAM
Climate Data Analyzer (CDA) muncul sebagai sebuah program yang dirancang khusus untuk memberikan bantuan dalam menganalisis data perubahan iklim. CDA memberikan kemudahan bagi pengguna untuk mengakses, memproses, dan menganalisis data iklim yang telah direkam dengan tujuan memberikan pemahaman yang lebih dalam tentang tren iklim di suatu kota atau wilayah tertentu. Dengan demikian, CDA menjadi sebuah alat yang sangat berharga bagi para peneliti, ilmuwan, dan pengambil kebijakan dalam upaya mereka untuk memahami dan mengatasi tantangan yang dihadapi akibat perubahan iklim.

Dirancang dengan bahasa pemograman Python dan Diintegrasikan dengan Database untuk menyimpan data dan informasi pada setiap entitas dengan menggunakan database MySQL sehingga memberikan efisien dan kenyamanan pada pengguna.

##
### B. STRUKTUR PROJECT
**1. Controller** : Digunakan untuk memberikan kontrol algoritma dan fungsi pada program dan menambahkan fungsi fitur dan jalannya program.
- Account Controller : disini merupakan algoritma dan jalannya program pada Login dan Registarasi.
- Admin Controller : terdapat 3 File yang sama sama memberikan kontrol algoritma pada admin seperti CRUD pada entitas user,data iklim dan data kota.
- User Controller : Menjalankan dan mengatur Informasi Data dan alur program ke pada user sehingga user dapat menggunakan fitur fitur program yang disediakan.
- Linked List Controller : Mengatur algoritma struktur data linked list seperti penambahan, penghapusan,clear dan manipulasi data lain pada linked list.

**2. Model** : Digunakan untuk API/Koneksi menuju sistem Program.
- DB MySQL : Melakukan Koneksi dari Program Python menuju Database MySQL.

**3. View** : Digunakan untuk tempat penampilan program yang diintegrasikan dengan algoritman Controller.
- Main View : Tempat penampilan Menu login dan Registrasi.
- Admin View : Tempat penampilan untuk CRUD setiap entitas beserta melakukan direct ke Controller.
- User View : Menjalankan dan mengatur Tampilan Informasi Data dan alur program untuk User seperti Informasi Iklim,Informasi Kota,Informasi Akun.

##
### C. FITUR DAN FUNGSIONALITAS
Adapula Modul Library yang digunakan dalam Program ini yaitu :
- PrettyTable : digunakan untuk membuat tabel ASCII dengan format yang menarik secara visual.
- OS : menyediakan cara untuk berinteraksi dengan sistem operasi.
- SYS : Digunakan untuk parameter spesifik sistem dan fungsi.
- mysql.connector : digunakan untuk menghubungkan aplikasi Python dengan basis data MySQL.
- PWInput : digunakan untuk memasukkan kata sandi secara aman dari pengguna.
- Time : Menyediakan berbagai fungsi terkait waktu dalam Python, contohnya yaitu sleep.
- Math : Digunakan untuk melakukan berbagai perhitungan matematika dalam bahasa pemrograman Python.
### PENJELASAN PROGRAM
#
### MODEL
Model - db_mysql.py
```
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect (
    host=os.getenv("DB_HOST"), 
    database=os.getenv("DB_NAME"), 
    user=os.getenv("DB_USER"), 
    password=os.getenv("DB_PASSWORD"), 
    port=os.getenv("DB_PORT"))
```
Line Code ini membuat koneksi ke database MySQL menggunakan Python. Dengan menggunakan modul mysql.connector untuk mengelola koneksi dan modul os untuk mengakses variabel lingkungan. Pengaturan environment variable dilakukan dengan dotenv untuk menyimpan informasi sensitif seperti nama host, nama database, username, dan password. Dengan menggunakan variabel lingkungan, informasi sensitif tidak ditampilkan langsung dalam kode, meningkatkan keamanan aplikasi.

#
### VIEW
View - main_view.py
```
from Controller import account_controller
import os
import time
import sys

def welcome():
    os.system("Cls")
    print("""
    ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
        ░█▀▀█ █── ─▀─ █▀▄▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ░█▀▀▄ █▀▀█ ▀▀█▀▀ █▀▀█ 　 ─█▀▀█ █▀▀▄ █▀▀█ █── █──█ ▀▀█ █▀▀ █▀▀█ 
        ░█─── █── ▀█▀ █─▀─█ █▄▄█ ──█── █▀▀ 　 ░█─░█ █▄▄█ ──█── █▄▄█ 　 ░█▄▄█ █──█ █▄▄█ █── █▄▄█ ▄▀─ █▀▀ █▄▄▀ 
        ░█▄▄█ ▀▀▀ ▀▀▀ ▀───▀ ▀──▀ ──▀── ▀▀▀ 　 ░█▄▄▀ ▀──▀ ──▀── ▀──▀ 　 ░█─░█ ▀──▀ ▀──▀ ▀▀▀ ▄▄▄█ ▀▀▀ ▀▀▀ ▀─▀▀
    ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
    """)

def menu():
    print("""
    ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
            Menu Utama
    ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
        1. Registrasi
        2. Login
        3. Keluar
    ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
    """)

def loading():
    print("Loading...", end='', flush=True)
    for i in range(11):
        time.sleep(0.3)
        print("\r█" + "█" * i + "▒" * (10 - i) + f"{10 * i}%", end='', flush=True)
    print("\n")

import sys

def mainProgram(): #Program Utama
    while True:
        try:
            welcome()
            loading()
            welcome()
            menu()
            menu_input = int(input("» Input Pilihan anda: "))
            if menu_input == 1:
                account_controller.registrasiUser()
            elif menu_input == 2:
                account_controller.login()
                time.sleep(2)
            elif menu_input == 3:
                print("Anda Keluar Program")
                break
        except KeyboardInterrupt:
            print("\nCtrl+C terdeteksi! Silakan gunakan menu untuk keluar dari program.")
            while True:
                try:
                    confirm = input("Apakah Anda yakin ingin keluar? (y/n): ").lower()
                    if confirm == 'y':
                        sys.exit()
                    elif confirm == 'n':
                        break
                    else:
                        print("Pilihan tidak valid. Silakan pilih 'y' untuk keluar atau 'n' untuk kembali.")
                except KeyboardInterrupt:
                    print("\nCtrl+C terdeteksi! Silakan gunakan menu untuk keluar dari program.")
```
**def welcome()** yang berfungsi bertanggung jawab untuk menampilkan pesan selamat datang dalam bentuk ASCII art. **def menu()** yang berfungsi digunakan untuk menampilkan menu utama aplikasi kepada pengguna. **def loading()** Fungsi ini menampilkan animasi loading yang memberikan umpan balik visual kepada pengguna tentang proses yang sedang berlangsung. Dan **def mainProgram()** berfungsi utama yang mengatur logika aplikasi. Menampilkan pesan-pesan awal dan menu utama menggunakan fungsi welcome(), loading(), dan menu(). Menggunakan loop untuk terus menampilkan menu hingga pengguna memilih untuk keluar. Menangani pengecualian KeyboardInterrupt untuk memastikan keluar dari program dengan aman menggunakan keyboard shortcut Ctrl+C.
#

View - admin_view.py
```
import os
import time
from Controller import useracc_controller, dataKota_controller, dataIklim_controller
from View import main_view

def viewUser():
    while True:
        os.system("cls")
        print("""
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
                Data User
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
            1. Tambah User
            2. Lihat User
            3. Update User
            4. Hapus User
            5. Kembali
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
        """)
        opsi = input("» Pilih Opsi yang tersedia (1/2/3/4/5): ")

        if opsi == '1':
            useracc_controller.tambahUser()
        elif opsi == '2':
            useracc_controller.lihatUser()
        elif opsi == '3':
            useracc_controller.updateUser()
        elif opsi == '4':
            useracc_controller.hapusUser()
        elif opsi == '5':
            print("Kembali ke menu utama...")
            time.sleep(0.5)
            return

def viewKota():
    while True:
        os.system("cls")
        print("""
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
                Data Kota
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
            1. Tambah Kota
            2. Lihat Kota
            3. Update Kota
            4. Hapus Kota
            5. Kembali
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
        """)
        opsi = input("» Pilih Opsi yang tersedia (1/2/3/4/5): ")

        if opsi == '1':
            dataKota_controller.tambahKota()
        elif opsi == '2':
            dataKota_controller.lihatKota()
        elif opsi == '3':
            dataKota_controller.updateKota()
        elif opsi == '4':
            dataKota_controller.hapusKota()
        elif opsi == '5':
            print("Kembali ke menu utama...")
            time.sleep(0.5)
            return

def viewIklim():
    while True:
        os.system("cls")
        print("""
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
                Data Iklim
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
            1. Tambah Iklim
            2. Lihat Iklim
            3. Update Iklim
            4. Hapus Iklim
            5. Kembali
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
        """)
        opsi = input("» Pilih Opsi yang tersedia (1/2/3/4/5): ")

        if opsi == '1':
            dataIklim_controller.tambahIklim()
        elif opsi == '2':
            dataIklim_controller.lihatIklim()
        elif opsi == '3':
            dataIklim_controller.updateIklim()
        elif opsi == '4':
            dataIklim_controller.hapusIklim()
        elif opsi == '5':
            print("Kembali ke menu utama...")
            time.sleep(0.5)
            return

def menuAdmin():
    try:
        os.system("cls")
        print("""
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
                Admin Menu
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
            1. Data User
            2. Informasi Kota
            3. Data Iklim
            4. Keluar
        ▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌
        """)
        opsi = input("» Pilih Opsi yang tersedia (1/2/3/4): ")
        if opsi == "1":
            viewUser()
        elif opsi == "2":
            viewKota()
        elif opsi == "3":
            viewIklim()
        elif opsi =="4":
            main_view.mainProgram()
    except KeyboardInterrupt:
        print("\nTerjadi Kesalahan!")
        exit()
```
Fungsi menuAdmin() menampilkan menu admin. Setelah itu, meminta admin untuk memilih opsi (1-4). Opsi dipilih dengan memasukkan nomor yang sesuai. Jika dipilih opsi 1, viewUser() dipanggil. Jika opsi 2, viewKota(). Jika opsi 3, viewIklim(). Jika opsi 4, kembali ke menu utama dengan memanggil main_view.mainProgram(). Tangani pengecualian KeyboardInterrupt, jika terjadi, keluar dari program dengan pesan kesalahan.
