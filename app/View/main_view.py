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
