from View import user_view,main_view
from Model import db_mysql
from Controller import linkedlist_controller
from prettytable import PrettyTable
import os
import time
import mysql.connector

LinkedList = linkedlist_controller.LinkedList()

def informasiIklim():
    user_view.lihatData()
    try:
        cursor = db_mysql.connection.cursor()
        query_count = "SELECT COUNT(*) FROM data_iklim"
        cursor.execute(query_count)
        total_rows = cursor.fetchone()[0]

        if total_rows == 0:
            print("Tidak ada iklim yang terdaftar.")
            return

        current_row = 0
        page = 1
        while current_row < total_rows:
            query_select = "SELECT * FROM data_iklim LIMIT 25 OFFSET %s"
            cursor.execute(query_select, (current_row,))
            hasil = cursor.fetchall()

            os.system("cls")
            print(f"Daftar Iklim - Halaman {page}:")
            pt = PrettyTable()
            pt.field_names = ["Nama Kota", "ID Iklim", "Kelembapan", "Curah Hujan", "Suhu Celcius", "Kecepatan Angin", "Kualitas Udara", "Rentan Tanggal"]
            for column in hasil:
                nama_kota = column[0][:20] + "..." if len(column[0]) > 23 else column[0]
                kelembapan = column[2][:20] + "..." if len(column[2]) > 23 else column[2]
                curah_hujan = column[3][:20] + "..." if len(column[3]) > 23 else column[3]
                suhu_celcius = column[4][:20] + "..." if len(column[4]) > 23 else column[4]
                kecepatan_angin = column[5][:20] + "..." if len(column[5]) > 23 else column[5]
                kualitas_udara = column[6][:20] + "..." if len(column[6]) > 23 else column[6]
                rentan_tanggal = column[7][:20] + "..." if len(column[7]) > 23 else column[7]
                pt.add_row([nama_kota, column[1], kelembapan, curah_hujan, suhu_celcius, kecepatan_angin, kualitas_udara, rentan_tanggal])
            print(pt)

            user_view.opsiLihatIklim()
            option = input("» Masukkan pilihan Anda: ") 

            if option == '1':
                current_row += 25
                page += 1
            elif option == '2':
                if page > 1:
                    current_row -= 25
                    page -= 1
                else:
                    os.system("cls")
                    print("Anda sudah berada di halaman pertama.")
                    time.sleep(1)
            elif option == '3':
                sortingIklim()
            elif option == '4':
                searchingIklim()
            elif option == '5':
                return
            else:
                print("Pilihan tidak valid.")
    except mysql.connector.Error as err:
        print("Error:", err)

def searchingIklim():
    os.system("cls")
    ambilDataIklim()

    keyword = input("Masukkan Kota yang ingin dicari: ").lower()
    found_kota = LinkedList.jumpSearch(keyword, "nama_kota")

    if found_kota:
        tabel = PrettyTable()
        tabel.field_names = ["Nama Kota", "ID Iklim", "Kelembapan", "Curah Hujan", "Suhu Celcius", "Kecepatan Angin", "Kualitas Udara", "Rentan Tanggal"]
        tabel.add_row([found_kota["nama_kota"], found_kota["id_iklim"], found_kota["kelembapan"], found_kota["curah_hujan"], found_kota["suhu_celcius"], found_kota["kecepatan_angin"],  found_kota["kualitas_udara"], found_kota["rentan_tanggal"]])
        print(tabel)
    else:
        print("Data tidak ditemukan.")
    input("Tekan enter untuk melanjutkan...")

def sortingIklim():
    os.system("cls")
    LinkedList.clear()
    ambilDataIklim()
    daftarIklim = []
    current = LinkedList.head
    while current:
        current.data["nama_kota"] = current.data["nama_kota"].lower()
        daftarIklim.append(current.data)
        current = current.next

    print("Pilih urutan pengurutan:")
    print("1. Ascending (A-Z)")
    print("2. Descending (Z-A)")
    urutan = input("» Masukkan pilihan Anda: ")

    if urutan == '1':
        sortedIklim = sorted(daftarIklim, key=lambda x: x["nama_kota"])
    elif urutan == '2':
        sortedIklim = sorted(daftarIklim, key=lambda x: x["nama_kota"], reverse=True)
    else:
        print("Pilihan tidak valid.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["Nama Kota", "ID Iklim", "Kelembapan", "Curah Hujan", "Suhu Celcius", "Kecepatan Angin", "Kualitas Udara", "Rentan Tanggal"]
    for column in sortedIklim:
        nama_kota = column["nama_kota"]
        id_iklim = column["id_iklim"]
        kelembapan = user_view.potong_teks(column["kelembapan"], 20)
        curah_hujan = user_view.potong_teks(column["curah_hujan"], 20)
        suhu_celcius = user_view.potong_teks(column["suhu_celcius"], 20)
        kecepatan_angin = user_view.potong_teks(column["kecepatan_angin"], 20)
        kualitas_udara = user_view.potong_teks(column["kualitas_udara"], 20)
        rentan_tanggal = user_view.potong_teks(column["rentan_tanggal"], 20)
        tabel.add_row([nama_kota, id_iklim, kelembapan, curah_hujan, suhu_celcius, kecepatan_angin, kualitas_udara, rentan_tanggal])
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

def ambilDataIklim():
    try:
        LinkedList.clear()
        query = "SELECT * FROM data_Iklim"
        cursor = db_mysql.connection.cursor()
        cursor.execute(query)
        hasil = cursor.fetchall()
        for column in hasil:
            dataIklim = {
                "nama_kota": column[0],
                "id_iklim": column[1],
                "kelembapan": column[2],
                "curah_hujan": column[3],
                "suhu_celcius": column[4],
                "kecepatan_angin": column[5],
                "kualitas_udara": column[6],
                "rentan_tanggal": column[7]
            }
            LinkedList.insert(dataIklim)
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def informasiKota():
    user_view.lihatData()
    try:
        cursor = db_mysql.connection.cursor()
        query_count = "SELECT COUNT(*) FROM data_kota"
        cursor.execute(query_count)
        total_rows = cursor.fetchone()[0]

        if total_rows == 0:
            print("Tidak ada kota yang terdaftar.")
            return

        current_row = 0
        page = 1
        no = 1 
        while current_row < total_rows:
            query_select = "SELECT * FROM data_kota LIMIT 25 OFFSET %s"
            cursor.execute(query_select, (current_row,))
            hasil = cursor.fetchall()
            
            os.system("cls")
            print(f"Daftar Kota - Halaman {page}:")
            pt = PrettyTable()
            pt.field_names = ["No", "Nama Kota", "Provinsi", "Deskripsi Iklim", "Struktur Kota", "Populasi"]
            for kota in hasil:
                pt.add_row([no, kota[0], kota[1], kota[2], kota[3], kota[4]])
                no += 1 
            print(pt)

            user_view.opsiLihatKota()
            option = input("» Masukkan pilihan Anda: ")

            if option == '1':
                current_row += 25
                page += 1
            elif option == '2':
                if page > 1:
                    current_row -= 25
                    page -= 1
                else:
                    os.system("cls")
                    print("Anda sudah berada di halaman pertama.")
                    time.sleep(1)
            elif option == '3':
                sortingKota()
            elif option == '4':
                searchingKota()
            elif option == '5':
                return
            else:
                print("Pilihan tidak valid.")
    except mysql.connector.Error as err:
        print("Error:", err)

def searchingKota():
    os.system("cls")
    ambilDataKota()

    print("Pilih jenis pencarian:")
    print("1. Search by Nama Kota")
    print("2. Search by Provinsi")
    option = input("» Masukkan pilihan Anda: ")

    if option == '1':
        keyword = input("Masukkan Kota yang ingin dicari: ").lower()
        found_kota = LinkedList.jumpSearch(keyword, "nama_kota")
    elif option == '2':
        keyword = input("Masukkan Provinsi yang ingin dicari: ").lower()
        query_select = "SELECT * FROM data_kota WHERE LOWER(provinsi) = %s"
        cursor = db_mysql.connection.cursor()
        cursor.execute(query_select, (keyword,))
        provinsi = cursor.fetchall()

        if not provinsi:
            print("Data tidak ditemukan.")
            return

        print(f"Data Provinsi '{keyword.capitalize()}':")
        pt = PrettyTable()
        pt.field_names = ["No", "Nama Kota", "Provinsi", "Deskripsi Iklim", "Struktur Kota", "Populasi"]
        no = 1
        for column in provinsi:
            pt.add_row([no, column[0], column[1], column[2], column[3], column[4]])
            no += 1
        print(pt)

        print(f"Total Data dari {keyword.capitalize()}: {len(provinsi)}")
        input("Tekan enter untuk melanjutkan...")
        return
    else:
        print("Pilihan tidak valid.")
        return

    if found_kota:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Kota", "Provinsi", "Deksripsi Iklim", "Struktur Kota", "Populasi"]
        tabel.add_row([1, found_kota["nama_kota"], found_kota["provinsi"], found_kota["deskripsi_iklim"], found_kota["struktur_kota"], found_kota["populasi"]])
        print(tabel)
    else:
        print("Data tidak ditemukan.")
    input("Tekan enter untuk melanjutkan...")

def sortingKota():
    os.system("cls")
    LinkedList.clear()
    ambilDataKota()
    daftarKota = []
    current = LinkedList.head
    no = 1
    while current:
        current.data["nama_kota"] = current.data["nama_kota"].lower()
        daftarKota.append(current.data)
        current = current.next

    print("Pilih urutan pengurutan:")
    print("1. Ascending (A-Z)")
    print("2. Descending (Z-A)")
    urutan = input("» Masukkan pilihan Anda: ")

    if urutan == '1':
        sortedKota = sorted(daftarKota, key=lambda x: x["nama_kota"])
    elif urutan == '2':
        sortedKota = sorted(daftarKota, key=lambda x: x["nama_kota"], reverse=True)
    else:
        print("Pilihan tidak valid.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Kota", "Provinsi", "Deskripsi Iklim", "Struktur Kota", "Populasi"]
    for column in sortedKota:
        tabel.add_row([no, column["nama_kota"], column["provinsi"], column["deskripsi_iklim"], column["struktur_kota"], column["populasi"]])
        no += 1
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

def ambilDataKota():
    try:
        LinkedList.clear()
        query = "SELECT * FROM data_kota"
        cursor = db_mysql.connection.cursor()
        cursor.execute(query)
        hasil = cursor.fetchall()
        for kota in hasil:
            dataKota = {
                "nama_kota": kota[0],
                "provinsi": kota[1],
                "deskripsi_iklim": kota[2],
                "struktur_kota": kota[3],
                "populasi": kota[4]
            }
            LinkedList.insert(dataKota)
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")