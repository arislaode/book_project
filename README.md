# Spesifikasi Project:
  - Python 3.5.2
  - Django 2.2.10
  - Postgresql 12.1
  - Restframework 3.11.0
  - Oauth2client 4.1.3
  - Ubuntu 18.04

# CRUD Book Library

  - Buat nama database dengan nama "TestDB" di postgresql

  - Setting database menggunakan postgresql:

		'default': {
		    'ENGINE': 'django.db.backends.postgresql',
		    'NAME': 'TestDB',
		    'USER':'root',
		    'PASSWORD':'root',
		    'HOST':'localhost'
		}

  - Jalankan perintah --> python manage.py makemigrations book_register

  - File tergenerate otomatis "migrations/0001_initial.py" 

  - Jalankan perintah --> python manage.py sqlmigrate book_register 0001

  - Jalankan perintah --> python manage.py migrate

  - Masukkan data pada tabel "book_register_booklist" dengan query berikut:

		INSERT INTO book_register_booklist (title) VALUES
		    ('Extreme Book Python'),
		    ('Code with python'),
		    ('Enjoy Book Python'),
		    ('Clean Code Python'),
		    ('OOP Book Python');

  - Buka url http://127.0.0.1:8000/book/ , Isi form untuk peminjaman buku.

  - Buka url http://127.0.0.1:8000/book/list/ , untuk melihat data buku yang dipinjam

  - Ubah dan hapus data list buku sesuai kebutuhan.

# Rest API & Authentication

  - Untuk mengecek Rest API , buka link http://127.0.0.1:8000/api/order/

  - Jika anda mendapat pesan "detail": "Authentication credentials were not provided." , maka anda perlu melakukan autentikasi untuk mendapat akses.

  - Jalankan terlebih dahulu project Book Library --> python manage runserver

  - Buat superuser terlebih dahulu dengan perintah: 
    --> python manage.py createsuperuser

  - Silahkan isi username, email dan password nya. misal, username= myuser, email= myuser@gmail.com, password: password.

  - Buka terminal baru, masukan username & password untuk mendapatkan token dengan perintah :
    --> http POST http://localhost:8000/api-token-auth username="myuser" password="password" 

  - Note : username & password bisa dicustomize

  - Copy token yang telah di generate, misal : 307b2eb5d3bb93773797b4e42a4429f5429e3958

  - Lakukan authorisasi dengan perintah :
    --> http http://127.0.0.1:8000/api/order/ "Authorization: Token 307b2eb5d3bb93773797b4e42a4429f5429e3958"

  - login pada browser dengan url --> http://127.0.0.1:8000/login/

  - Jika Error, tidak masalah. Silahkan buka kembali API nya --> http://127.0.0.1:8000/api/order/

  - Selamat jika berhasil. Cek kembali langkah diatas jika masih gagal.


# Set Order Book

  - Buat orderan untuk memesan buku yang ingin dibaca dengan mengisi fields: Name, Name book, Contact & Address

# Get Data Member
  - Get data membernya dengan membuka url berikut pada browser --> http://127.0.0.1:8000/api/order/1/