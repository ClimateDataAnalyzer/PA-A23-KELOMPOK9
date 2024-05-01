import os
from Controller import user_controller
from Model import db_mysql
from View import main_view

def menuUser(asal_kota, nickname, email):
    while True:
        cursor = db_mysql.connection.cursor()

        query = "SELECT * FROM data_iklim WHERE nama_kota = %s"
        cursor.execute(query, (asal_kota,))
        hasil = cursor.fetchone()

        if hasil:
            os.system("cls")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print("          SELAMAT DATANG DI         ")
            print("        CLIMATE DATA ANALYZER       ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print("      INFORMASI IKLIM KOTA ANDA     ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print(f"⋞⋞ Kota Anda: {hasil[0]}          ")
            print(f"⋞⋞ Kelembapan: {hasil[2]}         ")
            print(f"⋞⋞ Curah Hujan: {hasil[3]}        ")
            print(f"⋞⋞ Suhu Celcius: {hasil[4]}       ")
            print(f"⋞⋞ Kecepatan Angin: {hasil[5]}    ")
            print(f"⋞⋞ Kualitas Udara: {hasil[6]}     ")
            print(f"⋞⋞ Rentan Tanggal: {hasil[7]}     ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print("     MENU CLIMATE DATA ANALYZER     ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print("  1. Informasi Iklim Setiap Kota    ")
            print("  2. Informasi Kota                 ")
            print("  3. Informasi Saya                 ")
            print("  4. Keluar                         ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            opsi = input("» Pilih Opsi yang tersedia (1/2/3/4): ")
            if opsi == "1":
                user_controller.informasiIklim()
            elif opsi == "2":
                user_controller.informasiKota()
            elif opsi == "3":
                informasiAkun(asal_kota, nickname, email)
            elif opsi == "4":
                return
            else:
                print("Opsi Tidak Valid!")
        else:
            os.system("cls")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print("          SELAMAT DATANG DI         ")
            print("        CLIMATE DATA ANALYZER       ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print("      INFORMASI IKLIM KOTA ANDA     ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print("  Informasi Iklim untuk kota Anda   ")
            print("          belum tersedia.           ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            print("  1. Informasi Iklim Setiap Kota    ")
            print("  2. Informasi Kota                 ")
            print("  3. Informasi Saya                 ")
            print("  4. Keluar                         ")
            print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
            opsi = input("» Pilih Opsi yang tersedia (1/2/3/4): ")
            if opsi == "1":
                user_controller.informasiIklim()
            elif opsi == "2":
                user_controller.informasiKota()
            elif opsi == "3":
                informasiAkun(asal_kota, nickname, email)
            elif opsi == "4":
                return
            else:
                print("Opsi Tidak Valid!")
                input("Tekan enter untuk melanjutkan...")

def informasiAkun(asal_kota, nickname, email):
    os.system("cls")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("          INFORMASI AKUN          ")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("  Nickname   : ", nickname)
    print("  Email      : ", email)
    print("  Asal Kota  : ", asal_kota)
    input("\nTekan Enter untuk kembali ke menu...")

def lihatData():
    os.system("cls")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("        MEMUAT DATA        ")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    main_view.loading()

def opsiLihatIklim():
    print("\nOpsi:")
    print("1. Halaman Selanjutnya")
    print("2. Halaman Sebelumnya")
    print("3. Sorting Berdasarkan Nama Kota")
    print("4. Searching Nama Kota")
    print("5. Kembali")

def opsiLihatKota():
    print("\nOpsi:")
    print("1. Halaman Selanjutnya")
    print("2. Halaman Sebelumnya")
    print("3. Sorting Berdasarkan Kota")
    print("4. Searching")
    print("5. Kembali")

def potong_teks(teks, panjang_maks):
    if len(teks) > panjang_maks:
        return teks[:panjang_maks] + "..."
    return teks