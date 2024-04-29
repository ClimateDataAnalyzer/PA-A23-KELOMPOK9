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

def tambahData():
    os.system("cls")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("         TAMBAH DATA       ")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")

def lihatData():
    os.system("cls")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("         LIHAT DATA        ")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    main_view.loading()

def updateData():
    os.system("cls")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("         UPDATE DATA         ")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")

def hapusData():
    os.system("cls")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("         HAPUS DATA        ")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")

def opsiLihatUser():
    print("\nOpsi:")
    print("1. Halaman Selanjutnya")
    print("2. Halaman Sebelumnya")
    print("3. Sorting Berdasarkan Nickname")
    print("4. Searching")
    print("5. Kembali")

def opsiUpdateUser():
    print("\nPilih data yang ingin diperbarui:")
    print("1. Nickname")
    print("2. Email")
    print("3. Password")
    print("4. Asal Kota")
    print("5. Kembali ke Menu Utama")

def opsiLihatKota():
    print("\nOpsi:")
    print("1. Halaman Selanjutnya")
    print("2. Halaman Sebelumnya")
    print("3. Sorting Berdasarkan Kota")
    print("4. Searching")
    print("5. Kembali")

def opsiUpdateKota():
    print("\nPilih data yang ingin diperbarui:")
    print("1. Kota")
    print("2. Provisni")
    print("3. Deskripsi Iklim")
    print("4. Struktur Kota")
    print("6. Populasi")
    print("7. Kembali ke Menu Utama")

def opsiLihatIklim():
    print("\nOpsi:")
    print("1. Halaman Selanjutnya")
    print("2. Halaman Sebelumnya")
    print("3. Sorting Berdasarkan Nama Kota")
    print("4. Searching Nama Kota")
    print("5. Kembali")

def opsiUpdateIklim():
    print("\nPilih data yang ingin diperbarui:")
    print("1. Nama Kota")
    print("2. Kelembapan")
    print("3. Curah Hujan")
    print("4. Suhu Celcius")
    print("6. Kecepatan Angin")
    print("7. Kualitas Udara")
    print("8. Rentan Tanggal")
    print("9. Kembali ke Menu Utama")