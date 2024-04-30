import os
import sys
import time
import mysql.connector
from Model import db_mysql
from View import admin_view
from prettytable import PrettyTable
from Controller import linkedlist_controller

LinkedList = linkedlist_controller.LinkedList()

def tambahKota():
    admin_view.tambahData()
    input_nama = input("Berikan Nama Kota (Maksimal 30 kata): ").strip()
    input_provinsi = input("Berikan Provinsi (Maksimal 30 kata): ").strip()
    input_iklim = input("Berikan Deskripsi Iklim pada kota (Maksimal 255 kata): ").strip()
    input_struktur = input("Deskripsi Struktur Kota (Maksimal 255 kata): ").strip()
    
    while True:
        try:
            input_populasi = int(input("Isi Populasi (maksimal 11 digit): ").strip())
            if not (0 <= input_populasi <= 99999999999): 
                raise ValueError("Populasi harus berupa angka dengan maksimal 11 digit.")
                time.sleep(1)
            break
        except ValueError as ve:
            print("Error:", ve)
            time.sleep(1)

    if not input_nama or not input_provinsi or not input_iklim or not input_struktur:
        print("Data tidak boleh kosong.")
        time.sleep(1)
        return

    try:
        if len(input_nama) > 30 or len(input_provinsi) > 30:
            raise ValueError("Nama kota dan provinsi tidak boleh lebih dari 30 karakter.")
        if len(input_iklim) > 255 or len(input_struktur) > 255:
            raise ValueError("Deskripsi iklim dan struktur kota tidak boleh lebih dari 255 karakter.")

        new_kota = (input_nama, input_provinsi, input_iklim, input_struktur, input_populasi)

        linkedlist = linkedlist_controller.LinkedList()
        linkedlist.insert(new_kota)

        cursor = db_mysql.connection.cursor()
        query_check = "SELECT * FROM data_kota WHERE nama_kota = %s"
        cursor.execute(query_check, (input_nama,))
        existing_kota = cursor.fetchone()

        if existing_kota:
            print("Kota sudah ada. Silakan gunakan yang lain.")
            time.sleep(1)
            return
        else:
            query_insert = "INSERT INTO data_kota (nama_kota, provinsi, deskripsi_iklim, struktur_kota, populasi) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query_insert, new_kota)
            db_mysql.connection.commit()
            print("Kota berhasil ditambahkan ke database.")
    except mysql.connector.Error as err:
        print("Error:", err)
    except ValueError as ve:
        print("Error:", ve)

def lihatKota():
    admin_view.lihatData()
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

            admin_view.opsiLihatKota()
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

def updateKota():
    admin_view.updateData()
    keyword = input("Masukkan Nama Kota yang ingin diperbarui: ").strip()

    try:
        cursor = db_mysql.connection.cursor()
        query_select = "SELECT * FROM data_kota WHERE nama_kota = %s"
        cursor.execute(query_select, (keyword,))
        kota = cursor.fetchone()

        if not kota:
            print("Data tidak ditemukan.")
            time.sleep(1)
            return
        admin_view.opsiUpdateKota()
        option = input("» Masukkan pilihan Anda: ")

        if option == '1':
            new_kota = input("Masukkan Nama Kota baru: ").strip()
            if not new_kota:
                print("Nama Kota tidak boleh kosong.")
                time.sleep(1)
                return
            check_query = "SELECT * FROM data_kota WHERE nama_kota = %s"
            cursor.execute(check_query, (new_kota,))
            existing_kota = cursor.fetchone()
            if existing_kota:
                print("Nama Kota sudah digunakan. Silakan gunakan yang lain.")
                time.sleep(1)
            else:
                update_query = "UPDATE data_kota SET nama_kota = %s WHERE nama_kota = %s"
                cursor.execute(update_query, (new_kota, kota[0]))
                db_mysql.connection.commit()
                print("Nama Kota berhasil diperbarui.")
                time.sleep(1)
        elif option == '2':
            new_provinsi = input("Masukkan Provinsi baru: ").strip()
            if not new_provinsi:
                print("Provinsi tidak boleh kosong.")
                time.sleep(1)
                return
            update_query = "UPDATE data_kota SET provinsi = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_provinsi, kota[0]))
            db_mysql.connection.commit()
            print("Provinsi berhasil diperbarui.")
            time.sleep(1)
        elif option == '3':
            new_iklim = input("Masukkan Deskripsi Iklim baru: ").strip()
            if not new_iklim:
                print("Deskripsi Iklim tidak boleh kosong.")
                time.sleep(1)
                return
            update_query = "UPDATE data_kota SET deskripsi_iklim = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_iklim, kota[0]))
            db_mysql.connection.commit()
            print("Deskripsi Iklim berhasil diperbarui.")
            time.sleep(1)
        elif option == '4':
            new_struktur = input("Masukkan Struktur Kota baru: ").strip()
            if not new_struktur:
                print("Struktur Kota tidak boleh kosong.")
                time.sleep(1)
                return
            update_query = "UPDATE data_kota SET struktur_kota = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_struktur, kota[0]))
            db_mysql.connection.commit()
            print("Struktur Kota berhasil diperbarui.")
            time.sleep(1)
        elif option == '5':
            new_populasi = input("Masukkan Populasi baru: ").strip()
            if not new_populasi:
                print("Populasi tidak boleh kosong.")
                time.sleep(1)
                return
            update_query = "UPDATE data_kota SET populasi = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_populasi, kota[0]))
            db_mysql.connection.commit()
            print("Populasi berhasil diperbarui.")
            time.sleep(1)
        elif option == '6':
            return
        else:
            print("Pilihan tidak valid.")
    except mysql.connector.Error as err:
        print("Error:", err)

def hapusKota():
    admin_view.hapusData()
    keyword = input("Masukkan Kota pengguna yang ingin dihapus: ")

    try:
        cursor = db_mysql.connection.cursor()
        query_select = "SELECT * FROM data_kota WHERE nama_kota = %s"
        cursor.execute(query_select, (keyword,))
        kota = cursor.fetchone()

        if not kota:
            print("Data Kota tersebut tidak ditemukan.")
            return

        confirm = input(f"Apakah Anda yakin ingin menghapus Kota '{keyword}'? (y/n): ").lower()

        if confirm == 'y':
            delete_query = "DELETE FROM data_kota WHERE nama_kota = %s"
            cursor.execute(delete_query, (keyword,))
            db_mysql.connection.commit()
            print("Kota berhasil dihapus dari database.")
            time.sleep(1)
        elif confirm == 'n':
            print("Penghapusan dibatalkan.")
            time.sleep(1)
        else:
            print("Masukan tidak valid. Penghapusan dibatalkan.")
            time.sleep(1)
    except mysql.connector.Error as err:
        print("Error:", err)
        time.sleep(1)