import os
import sys
import time
import mysql.connector
from Model import db_mysql
from View import admin_view
from prettytable import PrettyTable
from Controller import linkedlist_controller

LinkedList = linkedlist_controller.LinkedList()

def tambahIklim():
    admin_view.tambahData()
    input_kota = str(input("Berikan Nama Kota (Maksimal 30 kata): ")).strip()
    if not input_kota:
        print("Nama Kota tidak boleh kosong.")
        return
    input_kelembapan = str(input("Deskripsi Kelembapan pada kota (Maksimal 255 kata): ")).strip()
    if not input_kelembapan:
        print("Deskripsi Kelembapan tidak boleh kosong.")
        return
    input_curahHujan = str(input("Deskripsi Curah Hujan Kota (Maksimal 255 kata): ")).strip()
    if not input_curahHujan:
        print("Deskripsi Curah Hujan tidak boleh kosong.")
        return
    input_suhuCelcius = str(input("Deskripsi Suhu Celcius (Maksimal 255 kata): ")).strip()
    if not input_suhuCelcius:
        print("Deskripsi Suhu Celcius tidak boleh kosong.")
        return
    input_kecepatanAngin = str(input("Deskripsi Kecepatan Angin (Maksimal 255 kata): ")).strip()
    if not input_kecepatanAngin:
        print("Deskripsi Kecepatan Angin tidak boleh kosong.")
        return
    input_kualitasUdara = str(input("Deskripsi Kualitas Udara (Maksimal 255 kata): ")).strip()
    if not input_kualitasUdara:
        print("Deskripsi Kualitas Udara tidak boleh kosong.")
        return
    input_rentanTanggal = str(input("Deskripsi Rentan Tanggal (Maksimal 255 kata): ")).strip()
    if not input_rentanTanggal:
        print("Deskripsi Rentan Tanggal tidak boleh kosong.")
        return

    try:
        if len(input_kota) > 30:
            raise ValueError("Nama Kota tidak boleh lebih dari 30 karakter.")
            time.sleep(1)
        if len(input_kelembapan) > 255 or len(input_curahHujan) > 255 or len(input_suhuCelcius) > 255 or len(input_kecepatanAngin) > 255 or len(input_kualitasUdara) > 255 or len(input_rentanTanggal) > 255:
            raise ValueError("Deskripsi tidak boleh lebih dari 255 karakter.")
            time.sleep(1)

        new_input = (input_kota, input_kelembapan, input_curahHujan, input_suhuCelcius, input_kecepatanAngin, input_kualitasUdara, input_rentanTanggal)

        linkedlist = linkedlist_controller.LinkedList()
        linkedlist.insert(new_input)

        cursor = db_mysql.connection.cursor()
        query_check = "SELECT * FROM data_iklim WHERE nama_kota = %s"
        cursor.execute(query_check, (input_kota,))
        existing_kota = cursor.fetchone()

        if existing_kota:
            print("Kota sudah ada. Silakan gunakan yang lain.")
            time.sleep(1)
            return
        else:
            query_insert = "INSERT INTO data_iklim (nama_kota, kelembapan, curah_hujan, suhu_celcius, kecepatan_angin, kualitas_udara, rentan_tanggal) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query_insert, new_input)
            db_mysql.connection.commit()
            print("Iklim berhasil ditambahkan ke database.")
            time.sleep(1)
    except mysql.connector.Error as err:
        print("Error:", err)
    except ValueError as ve:
        print("Error:", ve)

def lihatIklim():
    admin_view.lihatData()
    try:
        cursor = db_mysql.connection.cursor()
        query_count = "SELECT COUNT(*) FROM data_iklim"
        cursor.execute(query_count)
        total_rows = cursor.fetchone()[0]

        if total_rows == 0:
            print("Tidak ada iklim yang terdaftar.")
            time.sleep(1)
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
            
            # Menampilkan data dengan membatasi panjang karakter
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

            admin_view.opsiLihatIklim()
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

def potong_teks(teks, panjang_maks):
    if len(teks) > panjang_maks:
        return teks[:panjang_maks] + "..."
    return teks

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
        kelembapan = potong_teks(column["kelembapan"], 20)
        curah_hujan = potong_teks(column["curah_hujan"], 20)
        suhu_celcius = potong_teks(column["suhu_celcius"], 20)
        kecepatan_angin = potong_teks(column["kecepatan_angin"], 20)
        kualitas_udara = potong_teks(column["kualitas_udara"], 20)
        rentan_tanggal = potong_teks(column["rentan_tanggal"], 20)
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

def updateIklim():
    admin_view.updateData()
    keyword = input("Masukkan Nama Kota yang ingin diperbarui: ")

    try:
        cursor = db_mysql.connection.cursor()
        query_select = "SELECT * FROM data_kota WHERE nama_kota = %s"
        cursor.execute(query_select, (keyword,))
        kota = cursor.fetchone()

        if not kota:
            print("Data tidak ditemukan.")
            return

        admin_view.opsiUpdateIklim()
        option = input("» Masukkan pilihan Anda: ")

        if option == '1':
            new_kota = input("Masukkan Nama Kota baru: ").strip()
            if not new_kota:
                print("Nama Kota tidak boleh kosong.")
                time.sleep(1)
                return
            check_query = "SELECT * FROM data_iklim WHERE nama_kota = %s"
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
            new_kelembapan = input("Masukkan Deskripsi baru: ").strip()
            if not new_kelembapan:
                print("Data tidak boleh kosong.")
                time.sleep(1)
            update_query = "UPDATE data_iklim SET kelembapan = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_kelembapan, kota[0]))
            db_mysql.connection.commit()
            print("Deskripsi berhasil diperbarui.")
            time.sleep(1)
        elif option == '3':
            new_curahHujan = input("Masukkan Deskripsi baru: ").strip()
            if not new_curahHujan:
                print("Data tidak boleh kosong.")
                time.sleep(1)
            update_query = "UPDATE data_iklim SET curah_hujan = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_curahHujan, kota[0]))
            db_mysql.connection.commit()
            print("Deskripsi berhasil diperbarui.")
            time.sleep(1)
        elif option == '4':
            new_suhuCelcius = input("Masukkan Deskripsi baru: ").strip()
            if not new_suhuCelcius:
                print("Data tidak boleh kosong.")
                time.sleep(1)
            update_query = "UPDATE data_iklim SET suhu_celcius = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_suhuCelcius, kota[0]))
            db_mysql.connection.commit()
            print("Deskripsi berhasil diperbarui.")
            time.sleep(1)
        elif option == '5':
            new_kecepatanAngin = input("Masukkan Deskripsi baru: ").strip()
            if not new_kecepatanAngin:
                print("Data tidak boleh kosong.")
                time.sleep(1)
            update_query = "UPDATE data_iklim SET kecepatan_angin = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_kecepatanAngin, kota[0]))
            db_mysql.connection.commit()
            print("Deskripsi berhasil diperbarui.") 
            time.sleep(1)
        elif option == '6':
            new_kualitasUdara = input("Masukkan Deskripsi baru: ").strip()
            if not new_kualitasUdara:
                print("Data tidak boleh kosong.")
                time.sleep(1)
            update_query = "UPDATE data_iklim SET kualitas_udara = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_kualitasUdara, kota[0]))
            db_mysql.connection.commit()
            print("Deskripsi berhasil diperbarui.")
            time.sleep(1)
        elif option == '7':
            new_rentanTanggal = input("Masukkan Deskripsi baru: ").strip()
            if not new_rentanTanggal:
                print("Data tidak boleh kosong.")
                time.sleep(1)
            update_query = "UPDATE data_iklim SET rentan_tanggal = %s WHERE nama_kota = %s"
            cursor.execute(update_query, (new_rentanTanggal, kota[0]))
            db_mysql.connection.commit()
            print("Deskripsi berhasil diperbarui.")
            time.sleep(1)
        elif option == '9':
            return
        else:
            print("Pilihan tidak valid.")
    except mysql.connector.Error as err:
        print("Error:", err)

def hapusIklim():
    admin_view.hapusData()
    keyword = input("Masukkan Kota pengguna yang ingin dihapus: ")

    try:
        cursor = db_mysql.connection.cursor()
        query_select = "SELECT * FROM data_iklim WHERE nama_kota = %s"
        cursor.execute(query_select, (keyword,))
        kota = cursor.fetchone()

        if not kota:
            print("Data Iklim tersebut tidak ditemukan.")
            return

        confirm = input(f"Apakah Anda yakin ingin menghapus Data Iklim Kota '{keyword}'? (y/n): ").lower()

        if confirm == 'y':
            delete_query = "DELETE FROM data_iklim WHERE nama_kota = %s"
            cursor.execute(delete_query, (keyword,))
            db_mysql.connection.commit()
            print("Data Iklim berhasil dihapus dari database.")
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