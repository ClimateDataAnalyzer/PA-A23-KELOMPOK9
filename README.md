# PROJECT AKHIR A`23 KELOMPOK 9
## Program SDGs Climate Action (CLIMATE DATA ANALYZER)

### A. DESKRIPSI PROGRAM
Climate Data Analyzer (CDA) muncul sebagai sebuah program yang dirancang khusus untuk memberikan bantuan dalam menganalisis data perubahan iklim. CDA memberikan kemudahan bagi pengguna untuk mengakses, memproses, dan menganalisis data iklim yang telah direkam dengan tujuan memberikan pemahaman yang lebih dalam tentang tren iklim di suatu kota atau wilayah tertentu. Dengan demikian, CDA menjadi sebuah alat yang sangat berharga bagi para peneliti, ilmuwan, dan pengambil kebijakan dalam upaya mereka untuk memahami dan mengatasi tantangan yang dihadapi akibat perubahan iklim.

Dirancang dengan bahasa pemograman Python dan Diintegrasikan dengan Database untuk menyimpan data dan informasi pada setiap entitas dengan menggunakan database MySQL sehingga memberikan efisien dan kenyamanan pada pengguna.

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

### C. FITUR DAN FUNGSIONALITAS
Adapula Modul Library yang digunakan dalam Program ini yaitu :
- PrettyTable : digunakan untuk membuat tabel ASCII dengan format yang menarik secara visual.
- OS : menyediakan cara untuk berinteraksi dengan sistem operasi.
- SYS : Digunakan untuk parameter spesifik sistem dan fungsi.
- mysql.connector : digunakan untuk menghubungkan aplikasi Python dengan basis data MySQL.
- PWInput : digunakan untuk memasukkan kata sandi secara aman dari pengguna.
- Time : Menyediakan berbagai fungsi terkait waktu dalam Python, contohnya yaitu sleep.
- Math : Digunakan untuk melakukan berbagai perhitungan matematika dalam bahasa pemrograman Python.

Terdapat juga Penjelasan Program Yaitu :
### PENJELASAN PROGRAM
#### MODEL
Model - db_mysql.py
##
<tab><tab>code/text here

