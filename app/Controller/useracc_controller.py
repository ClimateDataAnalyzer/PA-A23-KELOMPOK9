import os
import sys
import time
import mysql.connector
from Model import db_mysql
from View import admin_view
from prettytable import PrettyTable
from Controller import linkedlist_controller

LinkedList = linkedlist_controller.LinkedList()

def tambahUser():
    admin_view.tambahData()
    input_nick = input("Berikan Nickname yang diinginkan : ").strip()
    input_email = input("Berikan Email yang diinginkan : ").strip()
    input_password = input("Berikan Password yang diinginkan : ").strip()
    input_askot = input("Berikan Kota Asal : ").strip()

    if not input_nick or not input_email or not input_password or not input_askot:
        print("Data tidak boleh kosong.")
        time.sleep(1)
        return

    try:
        new_user = (input_nick, input_email, input_password, input_askot)

        linkedlist = linkedlist_controller.LinkedList()
        linkedlist.insert(new_user)

        cursor = db_mysql.connection.cursor()
        query_check = "SELECT * FROM user WHERE nickname = %s"
        cursor.execute(query_check, (input_nick,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Nickname sudah digunakan. Silakan gunakan yang lain.")
            time.sleep(1)
            return
        else:
            query_insert = "INSERT INTO user (nickname, email, password, asal_kota) VALUES (%s, %s, %s, %s)"
            cursor.execute(query_insert, new_user)
            db_mysql.connection.commit()
            print("User berhasil ditambahkan ke database.")
    except mysql.connector.Error as err:
        print("Error:", err)
    except KeyboardInterrupt:
        print("Anda melakukan CTRL + C, Anda akan keluar program")
        sys.exit()

def lihatUser():
    admin_view.lihatData()    
    try:
        cursor = db_mysql.connection.cursor()
        query_count = "SELECT COUNT(*) FROM user"
        cursor.execute(query_count)
        total_rows = cursor.fetchone()[0]

        if total_rows == 0:
            print("Tidak ada pengguna yang terdaftar.")
            return

        current_row = 0
        page = 1
        while current_row < total_rows:
            query_select = "SELECT * FROM user LIMIT 25 OFFSET %s"
            cursor.execute(query_select, (current_row,))
            users = cursor.fetchall()
            
            os.system("cls")
            print(f"Daftar Pengguna - Halaman {page}:")
            pt = PrettyTable()
            pt.field_names = ["ID", "Nickname", "Email", "Password", "Kota Asal"]
            for user in users:
                pt.add_row([user[0], user[1], user[2],user [3], user[4]])
            print(pt)

            admin_view.opsiLihatUser()
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
                sortingUser()
            elif option == '4':
                searchingUser()
            elif option == '5':
                return
            
    except mysql.connector.Error as err:
        print("Error:", err)

def searchingUser():
    os.system("cls")
    ambilDataUser()

    print("Pilih jenis pencarian:")
    print("1. Search by Nickname")
    print("2. Search by Asal Kota")
    option = input("» Masukkan pilihan Anda: ")

    if option == '1':
        keyword = input("Masukkan Nickname yang ingin dicari: ").lower()
        found_user = LinkedList.jumpSearch(keyword, "nickname")
    elif option == '2':
        keyword = input("Masukkan Asal Kota yang ingin dicari: ").lower()
        query_select = "SELECT * FROM user WHERE LOWER(asal_kota) = %s"
        cursor = db_mysql.connection.cursor()
        cursor.execute(query_select, (keyword,))
        users = cursor.fetchall()

        if not users:
            print("Data tidak ditemukan.")
            return

        print(f"Pengguna dengan asal kota '{keyword.capitalize()}':")
        pt = PrettyTable()
        pt.field_names = ["ID User", "Nickname", "Email", "Password", "Asal Kota"]
        for user in users:
            pt.add_row([user[0], user[1], user[2], user[3], user[4]])
        print(pt)

        print(f"Total pengguna dari {keyword.capitalize()}: {len(users)}")
        input("Tekan enter untuk melanjutkan...")
        return
    else:
        print("Pilihan tidak valid.")
        return

    if found_user:
        tabel = PrettyTable()
        tabel.field_names = ["ID User", "Nickname", "Email", "Password", "Asal Kota"]
        tabel.add_row([found_user["id_user"], found_user["nickname"], found_user["email"], found_user["password"], found_user["asal_kota"]])
        print(tabel)
    else:
        print("Data tidak ditemukan.")
    input("Tekan enter untuk melanjutkan...")

def sortingUser():
    os.system("cls")
    LinkedList.clear()
    ambilDataUser()
    daftarUsers = []
    current = LinkedList.head
    while current:
        current.data["nickname"] = current.data["nickname"].lower()
        daftarUsers.append(current.data)
        current = current.next

    print("Pilih urutan pengurutan:")
    print("1. Ascending (A-Z)")
    print("2. Descending (Z-A)")
    urutan = input("» Masukkan pilihan Anda: ")

    if urutan == '1':
        sortedUsers = sorted(daftarUsers, key=lambda x: x["nickname"])
    elif urutan == '2':
        sortedUsers = sorted(daftarUsers, key=lambda x: x["nickname"], reverse=True)
    else:
        print("Pilihan tidak valid.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID User", "Nickname", "Email", "Password", "Asal Kota"]
    for user in sortedUsers:
        tabel.add_row([user["id_user"], user["nickname"], user["email"], user["password"], user["asal_kota"]])
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

def ambilDataUser():
    try:
        LinkedList.clear()
        query = "SELECT * FROM user"
        cursor = db_mysql.connection.cursor()
        cursor.execute(query)
        hasil = cursor.fetchall()
        for user in hasil:
            dataUser = {
                "id_user": user[0],
                "nickname": user[1],
                "email": user[2],
                "password": user[3],
                "asal_kota": user[4]
            }
            LinkedList.insert(dataUser)
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def updateUser():
    admin_view.updateData()
    nickname = input("Masukkan Nickname yang ingin diperbarui: ").strip()
    try:
        cursor = db_mysql.connection.cursor()
        query_select = "SELECT * FROM user WHERE nickname = %s"
        cursor.execute(query_select, (nickname,))
        user = cursor.fetchone()

        if not user:
            print("Nickname tidak ditemukan.")
            time.sleep(1)
            return

        admin_view.opsiUpdateUser()
        option = input("» Masukkan pilihan Anda: ")

        if option == '1':
            new_nickname = input("Masukkan Nickname baru: ").strip()
            if not new_nickname:
                print("Nickname tidak boleh kosong.")
                time.sleep(1)
                return
            check_query = "SELECT * FROM user WHERE nickname = %s"
            cursor.execute(check_query, (new_nickname,))
            existing_user = cursor.fetchone()
            if existing_user:
                print("Nickname sudah digunakan. Silakan gunakan yang lain.")
                time.sleep(1)
            else:
                update_query = "UPDATE user SET nickname = %s WHERE id_user = %s"
                cursor.execute(update_query, (new_nickname, user[0]))
                db_mysql.connection.commit()
                print("Nickname berhasil diperbarui.")
                time.sleep(1)
        elif option == '2':
            new_email = input("Masukkan Email baru: ").strip()
            if not new_email:
                print("Email tidak boleh kosong.")
                time.sleep(1)
                return
            update_query = "UPDATE user SET email = %s WHERE id_user = %s"
            cursor.execute(update_query, (new_email, user[0]))
            db_mysql.connection.commit()
            print("Email berhasil diperbarui.")
            time.sleep(1)
        elif option == '3':
            new_password = input("Masukkan Password baru: ").strip()
            if not new_password:
                print("Password tidak boleh kosong.")
                time.sleep(1)
                return
            update_query = "UPDATE user SET password = %s WHERE id_user = %s"
            cursor.execute(update_query, (new_password, user[0]))
            db_mysql.connection.commit()
            print("Password berhasil diperbarui.")
            time.sleep(1)
        elif option == '4':
            new_asal_kota = input("Masukkan Asal Kota baru: ").strip()
            if not new_asal_kota:
                print("Asal Kota tidak boleh kosong.")
                time.sleep(1)
                return
            update_query = "UPDATE user SET asal_kota = %s WHERE id_user = %s"
            cursor.execute(update_query, (new_asal_kota, user[0]))
            db_mysql.connection.commit()
            print("Asal Kota berhasil diperbarui.")
            time.sleep(1)
        elif option == '5':
            return
        else:
            print("Pilihan tidak valid.")
    except mysql.connector.Error as err:
        print("Error:", err)

def hapusUser():
    admin_view.hapusData()
    nickname = input("Masukkan Nickname pengguna yang ingin dihapus: ")
    try:
        cursor = db_mysql.connection.cursor()
        query_select = "SELECT * FROM user WHERE nickname = %s"
        cursor.execute(query_select, (nickname,))
        user = cursor.fetchone()

        if not user:
            print("Pengguna dengan Nickname tersebut tidak ditemukan.")
            return

        confirm = input(f"Apakah Anda yakin ingin menghapus pengguna '{nickname}'? (y/n): ").lower()

        if confirm == 'y':
            delete_query = "DELETE FROM user WHERE nickname = %s"
            cursor.execute(delete_query, (nickname,))
            db_mysql.connection.commit()
            print("Pengguna berhasil dihapus dari database.")
        elif confirm == 'n':
            print("Penghapusan dibatalkan.")
        else:
            print("Masukan tidak valid. Penghapusan dibatalkan.")
    except mysql.connector.Error as err:
        print("Error:", err)