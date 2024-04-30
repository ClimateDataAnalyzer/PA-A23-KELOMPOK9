from Model import db_mysql
from View import main_view
from View import admin_view
from View import user_view
import mysql.connector
import sys, os, pwinput

def registrasiUser():
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("              REGISTRASI AKUN             ")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    
    input_nick = input("Berikan Nickname yang anda inginkan : ").strip()
    input_email = input("Berikan Email anda : ").strip()
    input_password = pwinput.pwinput("Berikan Password anda : ").strip()
    input_askot = input("Dimana Kota anda berada : ").strip()

    # Validasi input
    if not input_nick or not input_email or not input_password or not input_askot:
        print("Gagal membuat akun. Pastikan semua informasi terisi.")
        input("Tekan Enter untuk kembali ke menu sebelumnya")
        main_view.mainProgram()
        return
    elif ' ' in input_nick or ' ' in input_email or ' ' in input_password or ' ' in input_askot:
        print("Gagal membuat akun. Nama pengguna, email, password, atau kota tidak boleh mengandung spasi.")
        input("Tekan Enter untuk kembali ke menu sebelumnya")
        main_view.mainProgram()
        return
    elif '@' not in input_email or input_email.count('@') != 1:
        print("Gagal membuat akun. Email harus mengandung simbol '@'.")
        input("Tekan Enter untuk kembali ke menu sebelumnya")
        main_view.mainProgram()
        return

    try:
        cursor = db_mysql.connection.cursor()

        query_check = "SELECT * FROM user WHERE nickname = %s"
        cursor.execute(query_check, (input_nick,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Akun dengan nickname tersebut sudah terdaftar. Silakan gunakan yang lain.")
            input("Tekan Enter untuk kembali ke menu sebelumnya")
            main_view.mainProgram()
        else:
            query = "INSERT INTO user (nickname, email, password, asal_kota) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (input_nick, input_email, input_password, input_askot))
            db_mysql.connection.commit()
            print("Registrasi Akun Berhasil")
            login_option =  input("Apakah Anda ingin login sekarang? (y/n): ").lower()
            if login_option == "y":
                main_view.loading()
                login()
            elif login_option == "n":
                print("Terima kasih telah mendaftar. Sampai jumpa!")
                sys.exit(0)
            else:
                print("Input tidak valid. Silakan pilih 'y' untuk login atau 'n' untuk keluar.")
    except mysql.connector.Error as err:
        print("Registrasi gagal:", err)
        input("Tekan Enter untuk kembali ke menu sebelumnya")
        main_view.mainProgram()

def login():
    os.system("cls")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    print("                  LOGIN                  ")
    print("▐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▌")
    
    input_attempts = 0
    while input_attempts < 3:
        input_nick = str(input("Nickname : "))
        input_password = pwinput.pwinput("Password : ")
        
        try:
            cursor = db_mysql.connection.cursor()
            query_check_user = "SELECT * FROM user WHERE nickname = %s AND password = %s"
            cursor.execute(query_check_user, (input_nick, input_password))
            existing_user = cursor.fetchone()

            if existing_user:
                os.system("cls")
                print("Login berhasil. Selamat datang, {}!".format(existing_user[1]))
                main_view.loading()
                nickname = existing_user[1]
                email = existing_user[2]
                asal_kota = existing_user[4]
                user_view.menuUser(asal_kota, nickname, email)
                return 
            else:
                query_check_admin = "SELECT * FROM admin WHERE username_admin = %s AND password = %s"
                cursor.execute(query_check_admin, (input_nick, input_password))
                existing_admin = cursor.fetchone()

                if existing_admin:
                    os.system("cls")
                    print("Login berhasil sebagai admin. Selamat datang, {}!".format(existing_admin[1]))
                    main_view.loading()
                    admin_view.menuAdmin()
                    return
                else:
                    print("Nickname atau password salah. Silakan coba lagi.")
                    input_attempts += 1

        except mysql.connector.Error as err:
            print("Error saat login:", err)
            input_attempts += 1

    print("Anda telah mencoba login lebih dari 3 kali. Kembali ke menu utama...")
    input("Tekan Enter untuk melanjutkan...")
    main_view.mainProgram()