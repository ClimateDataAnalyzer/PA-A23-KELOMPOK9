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
### FLOWCHART
![FLOWCHART PA drawio_compressed](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/dc15b4d0-434a-44e9-9ce0-c4f4d40fb8af)
#
### MODEL
- Model - db_mysql.py
```
import mysql.connector
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
- View - main_view.py
```
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
- View - admin_view.py
```
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
#
- View - user_view.py
```
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
            print(f"⋞⋞ Kelembapan: {hasil[1]}%         ")
            print(f"⋞⋞ Curah Hujan: {hasil[2]}        ")
            print(f"⋞⋞ Suhu Celcius: {hasil[3]}       ")
            print(f"⋞⋞ Kecepatan Angin: {hasil[4]}    ")
            print(f"⋞⋞ Kualitas Udara: {hasil[5]}     ")
            print(f"⋞⋞ Rentan Tanggal: {hasil[6]}     ")
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

def potong_teks(teks, panjang_maks):
    if len(teks) > panjang_maks:
        return teks[:panjang_maks] + "..."
    return teks
```
Fungsi menuUser(asal_kota, nickname, email) bertugas menampilkan menu pengguna pada aplikasi. Setelah menampilkan informasi iklim untuk kota pengguna, fungsi menampilkan menu pilihan: melihat informasi iklim dari kota lain, informasi tentang kota pengguna, informasi akun pengguna, atau keluar dari aplikasi. Jika informasi iklim untuk kota pengguna tidak tersedia, fungsi memberikan pesan yang sesuai. Fungsi informasiAkun(asal_kota, nickname, email) menampilkan informasi akun pengguna seperti nickname, email, dan asal kota. Fungsi potong_teks(teks, panjang_maks) digunakan untuk memotong teks jika panjangnya melebihi panjang maksimum yang ditentukan.
#
### Controller
- Controller - account_controller.py
```
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
```
Fungsi registrasiUser() bertanggung jawab untuk mendaftarkan pengguna baru. Pengguna diminta untuk memasukkan nickname, email, password, dan asal kota mereka. Validasi dilakukan untuk memastikan semua informasi terisi dengan benar. Jika tidak, pesan kesalahan akan ditampilkan. Setelah validasi, sistem akan memeriksa apakah nickname pengguna sudah ada dalam database. Jika sudah, pengguna diminta untuk memilih nickname yang lain. Jika belum, data pengguna baru akan dimasukkan ke dalam database. Setelah registrasi berhasil, pengguna diberikan opsi untuk langsung login atau keluar dari aplikasi.
```
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
```
Fungsi login() bertugas untuk proses login pengguna. Pengguna diminta untuk memasukkan nickname dan password. Sistem akan memeriksa kecocokan data dengan data yang tersimpan dalam database. Jika berhasil login, pengguna akan disambut dan diarahkan ke menu pengguna atau menu admin tergantung dari peran pengguna. Jika gagal login karena kesalahan memasukkan nickname atau password, pengguna diberikan kesempatan untuk mencoba lagi. Jika mencoba lebih dari 3 kali tanpa berhasil, pengguna akan dikembalikan ke menu utama.
#
- Controller - dataIklim_controller.py
```
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
```
Fungsi tambahIklim() bertanggung jawab untuk menambahkan data iklim baru ke dalam database. Administrator diminta untuk memasukkan informasi tentang nama kota, deskripsi kelembapan, curah hujan, suhu celcius, kecepatan angin, kualitas udara, dan rentan tanggal. Setiap input divalidasi untuk memastikan tidak kosong dan tidak melebihi batas karakter yang ditentukan. Jika data kota sudah ada dalam database, pesan kesalahan akan ditampilkan. Jika tidak, data akan dimasukkan ke dalam database.
```
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
```
Fungsi lihatIklim() digunakan untuk melihat daftar data iklim yang tersimpan dalam database. Data ditampilkan secara berurutan dengan membatasi jumlah data yang ditampilkan per halaman. Pengguna diberikan opsi untuk melihat halaman selanjutnya, halaman sebelumnya, melakukan sorting, melakukan pencarian, atau kembali ke menu sebelumnya.
```
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
```
Fungsi searchingIklim() digunakan untuk mencari data iklim berdasarkan nama kota yang diinputkan oleh pengguna. Data iklim akan ditampilkan jika ditemukan, jika tidak, pesan bahwa data tidak ditemukan akan muncul.
```
def potong_teks(teks, panjang_maks):
    if len(teks) > panjang_maks:
        return teks[:panjang_maks] + "..."
    return teks
```
Fungsi potong_teks() digunakan untuk memotong teks yang panjang menjadi teks yang lebih pendek dengan menambahkan elipsis (...) di akhir teks jika panjang teks melebihi panjang maksimal yang ditentukan.
```
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
```
Fungsi sortingIklim() memungkinkan administrator untuk melakukan sorting data iklim berdasarkan nama kota secara ascending (A-Z) atau descending (Z-A). Data akan ditampilkan setelah diurutkan.
```
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
```
Fungsi ambilDataIklim() digunakan untuk mengambil data iklim dari database dan memasukkannya ke dalam linked list.
```

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
```
Fungsi updateIklim() memungkinkan administrator untuk memperbarui informasi tentang data iklim. Administrator diminta untuk memilih kota yang akan diperbarui dan jenis informasi yang akan diperbarui. Kemudian, informasi baru dimasukkan dan diperbarui dalam database.
```
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
```
Fungsi hapusIklim() memungkinkan administrator untuk menghapus data iklim dari database. Administrator diminta untuk memilih kota yang akan dihapus, dan konfirmasi akan ditampilkan sebelum penghapusan dilakukan.
#
- Controller - dataKota_controller.py
```
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
```
Fungsi tambahKota() memungkinkan administrator untuk menambahkan data kota baru ke dalam database. Administrator diminta untuk memasukkan nama kota, provinsi, deskripsi iklim, struktur kota, dan populasi. Data yang dimasukkan akan divalidasi, dan jika sesuai, akan ditambahkan ke database.
```
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
```
Fungsi lihatKota() digunakan untuk menampilkan daftar kota yang terdaftar dalam database. Administrator dapat melihat kota-kota dalam halaman-halaman, mengatur sorting, dan melakukan pencarian.
```
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
```
Fungsi searchingKota() memungkinkan administrator untuk melakukan pencarian kota berdasarkan nama kota atau provinsi. Hasil pencarian akan ditampilkan jika data ditemukan.
```
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
```
Fungsi sortingKota() memungkinkan administrator untuk mengurutkan daftar kota berdasarkan nama kota secara ascending atau descending.
```
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
```
Fungsi ambilDataKota() digunakan untuk mengambil data kota dari database dan menyimpannya dalam linked list.
```
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
```
Fungsi updateKota() memungkinkan administrator untuk memperbarui informasi tentang kota yang ada dalam database.
```
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
```
Fungsi hapusKota() memungkinkan administrator untuk menghapus data kota dari database setelah konfirmasi.
#
- Controller - useracc_controller.py
```
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
```
Fungsi tambahUser() memungkinkan administrator untuk menambahkan pengguna baru ke dalam database. Administrator diminta untuk memasukkan nickname, email, password, dan kota asal pengguna. Data yang dimasukkan akan divalidasi, dan jika sesuai, akan ditambahkan ke database.
```
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
```
Fungsi lihatUser() digunakan untuk menampilkan daftar pengguna yang terdaftar dalam database. Administrator dapat melihat pengguna-pengguna dalam halaman-halaman, mengatur sorting, dan melakukan pencarian.
```
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
```
Fungsi searchingUser() memungkinkan administrator untuk melakukan pencarian pengguna berdasarkan nickname atau kota asal. Hasil pencarian akan ditampilkan jika data ditemukan.
```
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
```
Fungsi sortingUser() memungkinkan administrator untuk mengurutkan daftar pengguna berdasarkan nickname secara ascending atau descending.
```
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
```
Fungsi ambilDataUser() digunakan untuk mengambil data pengguna dari database dan menyimpannya dalam linked list.
```
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
```
Fungsi updateUser() memungkinkan administrator untuk memperbarui informasi tentang pengguna yang ada dalam database.
```
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
```
Fungsi hapusUser() memungkinkan administrator untuk menghapus data pengguna dari database setelah konfirmasi.
#
- Controller - linkedlist_controller.py
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
```
Class Node adalah representasi dari simpul dalam linked list. Setiap simpul memiliki dua atribut: data untuk menyimpan data dan next untuk menunjukkan ke simpul berikutnya dalam linked list.Dan Class LinkedList adalah implementasi dari linked list. Konstruktor __init__() membuat linked list kosong dengan menetapkan head (kepala) linked list menjadi None. Fungsi insert() digunakan untuk menyisipkan data baru ke dalam linked list. Jika linked list kosong, simpul baru dibuat dan diatur sebagai kepala. Jika tidak, fungsi akan mencari simpul terakhir dalam linked list dan menambahkan simpul baru setelahnya.
```
    def clear(self):
        self.head = None
```
Fungsi clear(self): Mengosongkan linked list dengan mengatur head menjadi None, sehingga semua simpul terhapus dari linked list.
```
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
```
Fungsi display(self): Menampilkan isi dari linked list dengan mengunjungi setiap simpul, dimulai dari head, dan mencetak datanya.
```
    def quickSort(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]

            less_than_pivot = [x for x in data[1:] if x <= pivot]
            greater_than_pivot = [x for x in data[1:] if x > pivot]

            return self.quickSort(less_than_pivot) + [pivot] + self.quickSort(greater_than_pivot)
```
Fungsi quickSort(self, data): Melakukan pengurutan data menggunakan algoritma Quicksort. Jika panjang data kurang dari atau sama dengan 1, data tersebut sudah terurut dan langsung dikembalikan. Jika tidak, elemen pertama (pivot) dipilih, kemudian data dibagi menjadi dua bagian: elemen yang lebih kecil dari atau sama dengan pivot, dan elemen yang lebih besar dari pivot. Kemudian, fungsi quickSort() diterapkan secara rekursif pada kedua bagian ini, dan hasilnya digabungkan dengan pivot di tengahnya.
```
    def jumpSearch(self, key, field):
        if not self.head:
            return None

        current = self.head
        while current:
            if current.data[field].lower() == key:
                return current.data
            current = current.next
        
        return None
```
Fungsi jumpSearch(self, key, field): Melakukan pencarian dalam linked list berdasarkan nilai kunci (key) dan bidang (field). Jika linked list kosong, fungsi mengembalikan None. Jika tidak, pencarian dilakukan dengan mengunjungi setiap simpul, dimulai dari head, dan memeriksa apakah nilai dalam bidang yang ditentukan sama dengan nilai kunci (dengan mengabaikan case sensitive). Jika ditemukan, fungsi mengembalikan data dari simpul tersebut. Jika tidak, fungsi mengembalikan None.
#
### Controller
- Controller - user_controller.py
```
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
```
Fungsi informasiIklim() adalah Menampilkan informasi mengenai iklim. Data iklim diambil dari database dan ditampilkan dalam bentuk tabel. Pengguna dapat memilih opsi untuk melihat data lebih lanjut, melakukan pencarian, atau mengurutkan data.
```
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
```
Fungsi searchingIklim() adalah Memungkinkan pengguna untuk melakukan pencarian data iklim berdasarkan nama kota. Hasil pencarian kemudian ditampilkan dalam bentuk tabel.
```
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
```
Fungsi sortingIklim() adalah Mengurutkan data iklim berdasarkan nama kota, baik secara ascending (A-Z) maupun descending (Z-A). Hasil pengurutan ditampilkan dalam bentuk tabel.
```
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
```
Fungsi ambilDataIklim() adalah Mengambil data iklim dari database dan memasukkannya ke dalam linked list. Data ini kemudian digunakan untuk pencarian dan pengurutan.
```
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
```
Fungsi informasiKota() adalah Menampilkan informasi mengenai kota. Data kota diambil dari database dan ditampilkan dalam bentuk tabel. Pengguna dapat memilih opsi untuk melihat data lebih lanjut, melakukan pencarian, atau mengurutkan data.
```
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
```
Fungsi searchingKota() adalah Memungkinkan pengguna untuk melakukan pencarian data kota berdasarkan nama kota atau provinsi. Hasil pencarian kemudian ditampilkan dalam bentuk tabel.
```
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
```
Fungsi sortingKota() adalah Mengurutkan data kota berdasarkan nama kota, baik secara ascending (A-Z) maupun descending (Z-A). Hasil pengurutan ditampilkan dalam bentuk tabel.
```
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
```
Fungsi ambilDataKota() adalah Mengambil data kota dari database dan memasukkannya ke dalam linked list. Data ini kemudian digunakan untuk pencarian dan pengurutan.

##
### D. CARA PENGGUNAAN
**PENGGUNAAN USER**
1. Dimenu awal user dapat memilih 3 pilihan yaitu register, login, dan keluar
- _Tampilan Menu Utama_

![Menu Utama](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/f9b8f713-2a54-4777-8ce8-872ededa4728)

2. Jika user memilih register maka user akan diminta untuk membuat akun dengan memasukkan _nickname, email, password,_ dan _asal kota_. Namun, jika user sudah memiliki akun user dapat langsung memilih pilihan login untuk masuk dengan akun yang sudah ada dengan menggunakan _nickname dan password_.
- _Tampilan Menu Register_

![Register](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/bda1f637-4809-4283-a0fd-660eed3f5e39)

- _Tampilan Menu Login_

![Login](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/ab7e5861-67e0-47a0-874a-84de91f2b7d1)

3. Jika user sudah berhasil Register dan melakukan Login, user akan ditampilkan data iklim dari asal kota mereka dan menu pilihan yaitu Informasi iklim setiap kota, Informasi kota, Informasi saya, dan keluar.
- _Tampilan Menu User_

![Menu User](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/fa265723-3dc2-4336-bf4f-d61445a8a5ca)

4. Jika user memilih Informasi iklim setiap kota maka user akan ditampilkan data iklim setiap kota yang ada. Selain ditampilkan data iklim setiap kota user juga akan mendapat beberapa pilihan lagi yaitu halaman selanjutnya, halaman sebelumnya, sorting berdasarkan Nama kota, searching nama kota, dan kembali. Pada bagian sorting terdapat pilihan ascending dan descending.

- _Tampilan Informasi Iklim_

![Informasi Iklim](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/3920e1a6-4845-4626-9f0e-9ac0ab0ab08f)

5. Jika user memilih Informasi kota maka user akan ditampilkan data-data kota yang ada. Setelah menampilkan data kota user juga akan mendapat beberapa pilihan lagi yaitu halaman selanjutnya, halaman sebelumnya, sorting berdasarkan Nama kota, searching nama kota, dan kembali. Pada bagian sorting terdapat pilihan ascending dan descending.

- _Tampilan Informasi Kota_

![Informasi Kota](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/7d0fb0a8-9765-4d13-9bcf-cc34c010e811)

6. Jika user memilih informasi saya maka user akan ditampilkan informasi mengenai nicknamenya, email, dan asal kota dari akun user tersebut.

- _Tampilan Informasi Akun_

![Informasi Akun](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/4bfd15a0-593e-442d-9b05-5571fe57f123)

7. Terakhir user dapat memilih keluar jika ingin keluar dari program dan kembali ke menu utama login dan register


**PENGGUNAAN ADMIN**
1. Saat pada bagian menu utama admin hanya perlu login dengan menggunakan akun admin yang tersedia.

2. Setelah berhasil login dengan akun admin, kalian akan diberikan tampilan menu admin dengan beberapa pilihan yaitu data user, informasi kota, data iklim, dan keluar.

- _Tampilan Menu Admin_

![Menu Admin](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/e50429ce-cf40-439f-8331-03cbbc5c333c)

3. Jika admin memilih data user maka akan ditampilkan pilihan Tambah User, Lihat user, Update user, Hapus user, dan keluar. Pada menu ini admin dapat melakukan CRUD pada data user.

- _Tampilan pada saat memilih data user_

![Pilih Data User](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/ca3cab0d-04fb-48be-a532-d5bb684cb3e3)

4. Jika admin memilih Informasi kota maka admin akan ditampilkan pilihan Tambah kota, Lihat kota, Update kota, Hapus kota, dan keluar. Pada menu ini admin dapat melakukan CRUD pada data kota.

- _Tampilan pada saat memilih Informasi Kota_

![Pilih Data Kota](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/4175ae7d-1e3e-48d7-a302-80c4939e00d8)

5. Jika admin memilih Data Iklim maka admin akan ditampilkan pilihan Tambah Iklim, Lihat Iklim, Update Iklim, Hapus Iklim, dan keluar. Pada menu ini admin dapat melakukan CRUD pada data iklim.

- _Tampilan pada saat memilih Data Iklim_

![Pilih Data Iklim](https://github.com/ClimateDataAnalyzer/PA-A23-KELOMPOK9/assets/144346363/e8be6973-b60f-4d1c-ae71-fb4e7938c5af)

6. Lalu admin juga dapat memilih keluar jika sudah ingin keluar dari menu admin dan kembali ke menu utama yaitu menu login 
