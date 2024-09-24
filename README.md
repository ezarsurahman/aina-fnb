<details>

 <summary>Tugas 2 PBP - Ezar Akhdan Shada Surahman</summary>

Markdown ini dibuat untuk memenuhi Tugas 2 PBP dengan nama aplikasi "Aina Homecook". `<br />` Link Deployment PWS : http://ezar-akhdan-ainafnb.pbp.cs.ui.ac.id/

## Step-by-step pengerjaan proyek

Berikut merupakan step-by-step pengerjaan proyek ini:

### Pembuatan Proyek Django

1. Saya membuat direktori `aina-fnb` pada laptop saya sebagai direktori untuk proyek ini.
2. Pada direktori `aina-fnb` saya menginstall virtual environment melalui terminal dengan command berikut:

   ```python
   python3 -m venv env
   ```
3. Setelah virtual environment terinstall, saya mengaktifkannya dengan commad:

   ```
   source env/bin/activate
   ```
4. Saya membuat file `requirements.txt` dengan isi sebagai berikut:

   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
5. Setelah itu saya melakukan dependencies pada `requirements.txt` dengan command:

   ```
   pip install -r requirements.tx
   ```
6. Lalu, saya melakukan instalansi project django dengan nama `aina_fnb` dengan command berikut:

   ```
   django-admin startproject aina_fnb .
   ```
7. Setelah proyek terinstall, saya menambahkan `"localhost"` dan `"127.0.0.1"` sebagai bagian dari `ALLOWED_HOST` pada file `settings.py`.

   ### Membuat aplikasi `main`
8. Saya membuat aplikasi baru bernama `main` dengan command:

   ```
   python manage.py startapp main
   ```

   #### Membuat Template
9. Setelah aplikasi main terinstall, saya menambahkan `'main'` ke list `INSTALLED_APPS` pada file `settings.py` sebagai penanda adanya aplikasi `main` ini.
10. Untuk membuat template, saya membuat direktori `templates` (di dalam direktori `main`) lalu menambahkan file `main.html` yang akan berperan sebagai templatenya.
11. Saya mengisi template dengan komponen-komponen yang dibutuhkan serta langsung menggunakan template variables untuk attrbute-attribute yang akan ditampilkan.

    ### Membuat Models
12. Setelah template, saya menambahkan sebuah model pada file `model.py`   yaitu `FoodEntry` yang memili attribute `name` , `price`, `ready`,dan  `description` serta sebuah read-only variable yaitu `is_pricy` untuk menentukan apakah sebuah makanan termasuk relatif mahal atau tidak.
13. Untuk mengaplikasikan model saya melakukan migration dengan dua command di bawah:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

    ### Menghubungkan View dengan Template
14. Selanjutnya, saya mengisi file `views.py `dengan sebuah function bernama `show_main` yang akan "mengirim" data ke template jika terdapat request dari template.
15. Data yang akan dikirim berupa atribut-atribut berupa atribut `name`,` price`, `ready, description`, `nama_aplikasi`, `nama_saya`, dan `kelas_saya`.

    ### Mengonfigurasi URL
16. Pertama, saya membuat file `urls.py` di dalam `main` dan menambahkan kode di bawah untuk mengonfigurasi routing pada aplikasi:

    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
17. Setelah itu, saya mengonfigurasi file `urls.py` yang berada pada `aina_fnb` untuk routing project keseluruhan dengan kode dibawah:

    ```
    ...
    from django.urls import path, include
    ...

    urlpatterns = [
        ...
        path('', include('main.urls')),
        ...
    ]
    ```

    ### Unit Tests
18. Selanjutnya, saya menambahkan beberapa unit tests pada `tests.py` yang bertujuan untuk memeriksa kebenaran kode, unit test yang dibuat meliputi:

    - Memeriksa apakah URL index (utama) bisa diakses
    - Memeriksa apakah halaman index (utama) dirender dengan template dari `main.html`
    - Memeriksa apakah halaman yang tidak ada pada project akan memberikan respons 404.
    - Memeriksa kebenaran read-only attributes yang ada di `models.py`
19. Untuk memeriksa kebenaran kode, saya menggunakan command:

    ```
    python manage.py test
    ```

### Git dan PWS Deployment

20. Saya membuat repository baru di github lalu menghubungkannya kepada repository yang ada pada lokal (melakukan `git init` terlebih dahulu)
21. Setelah terhubung, saya melakukan `add`, `commit`, dan `push` ke remote repository github
22. Untuk melakukan deployment ke PWS, pertama saya menambahkan URL repo saya ke list `ALLOWED_HOST` pada `settings.py`.
23. Terakhir, saya menyambungkan repository dengan PWS, lalu melakukan push ke repository PWS untuk melakukan deployment.

## Request client ke web aplikasi berbasis Django

[![Screenshot-2024-09-18-at-09-47-38.png](https://i.postimg.cc/6qy7Z9Yr/Screenshot-2024-09-18-at-09-47-38.png)](https://postimg.cc/RJxV5zrh)[![Screenshot-2024-09-18-at-09-47-38.png](https://i.postimg.cc/6qy7Z9Yr/Screenshot-2024-09-18-at-09-47-38.png)](https://postimg.cc/RJxV5zrh)

Secara singkat, saat user/client berinteraksi dengan website berbasis Django, maka device user akan mengirimkan sebuah HTTP request yang akan diarahkan oleh `urls.py` ke `views.py`. `views.py` memiliki peran penting untuk memilih data apa yang akan ditampilkan kepada user (bisa melalui database yang ada pada `models.py` maupun tidak) dan juga memilih template atau tampilan yang akan ditampilkan (berkas `html`).

`urls.py` -> mengarahkan user ke halaman yang sesuai.

`views.py` -> memilih data (`models.py`) serta tampilan/template (`main.html`) untuk diberikan kepada user

`models.py` -> sebagai database.

`main.html` -> sebagai tampilan/template untuk menampilkan data.

## Fungsi `git` dalam pengembangan perangkat lunak

`git` merupakan salah satu Version Control yang paling banyak digunakan. Berikut merupakan beberapa fungsi utama git:

- Version Control : `git` membuat pelacakan perubahan kode sangat mudah. Fitur ini sangat berguna saat developer memilki bug atau error lalu ingin melakukan debugging. Jika sudah "mentok", developer juga bisa mengembalikannya ke versi sebelumnya
- Collaborative : Dengan menggunakan layanan online seperti GitHub, developer bisa melakukan development secara bersamaan tanpa harus berada di tempat yang sama. Fitur Branching dan Merge pada `git` sangat berpengaruh dalam aspek kolaborasi.

Dengan Git, pengembangan perangkat lunak menjadi lebih terstruktur, efisien, dan terkelola dengan baik, terutama dalam tim besar atau proyek jangka panjang.

## Mengapa Django?

Menurut saya, salah satu faktor dipilihnya Django adalah karena bahasa pemorgramannya, yaitu Python. Python merupakan bahasa yang sudah dipelajari dari Semester 1. Sehingga, mahasiswa tidak perlu belajar syntax namun langsung fokus di konsep pemrograman berbasis platform. Selain itu, saya mengetahui bahwa Django merupakan framework yang sangat sering digunakan sehingga dokumentasi sudah lengkap dan komunitasnya sudah sangat luas.

## Kenapa models pada Django disebut sebagai ORM?

Models pada Django disebut sebagai ORM karena (Object Relational Mapping) karena sifat dari models yang mengonversi data menjadi tabel secara langsung. Akibatnya, developer tidak perlu berhubungan langsung dengan tabel-tabel data seperti SQL, namun bisa langsung membuat dan mengakses data dari model. `<br />`

Sekian jawaban dari saya. Terimakasih `<br />`

Salam `<br />`

Ezar

</details>

# Tugas 3

## Mengapa kita memerlukan Data Delivery?

Pada website yang menggunakan data dinamis, tentu sangat sulit dan banyak effort yang dilakukan jika kode `html` nya selalu diupdate berdasarkan input dari User. Oleh karena itu, kita membutuhkan data delivery agar penyampaian dan pengaksesan data dapat dilakukan secara otomatis dan real-time.

## JSON vs XML

Dibandingkan dengan XML, JSON lebih ringan, lebih mudah dibaca, dan lebih mudah ditulis oleh manusia serta lebih efisien untuk mesin. Karena JSON menggunakan struktur berbasis objek, JSON lebih sesuai untuk aplikasi web modern, terutama dalam komunikasi client-server. Di lain sisi, XML memiliki markup yang lebih kompleks dan lebih berat.

## `is_valid()` pada form Django

function `is_valid()` memastikan apakah semua field terisi dengan jenis datafield yang dibutuhkan dan tidak boleh ada field yang kosong. Sebenarnya, `is_valid()` juga bisa dibuat dengan settingan custom namun pada saat ini, `is_valid()` hanya digunakan untuk validasi datatype

## `csrf_token`: apa fungsinya?

Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang dapat mengeksploitasi sesi pengguna yang sah untuk menjalankan aksi berbahaya tanpa sepengetahuan pengguna. Jika kita tidak menambahkan `csrf_token`, aplikasi menjadi rentan terhadap serangan ini, di mana penyerang bisa memalsukan permintaan dari pengguna dengan cara mengirimkan form palsu dari domain yang berbeda. Tanpa validasi `csrf_token`, server tidak bisa membedakan apakah permintaan tersebut sah atau berasal dari sumber yang tidak valid, yang dapat menyebabkan perubahan data tanpa izin.

## Screenshot Postman

### XML semua object

<img width="1271" alt="Screenshot 2024-09-17 at 13 38 24" src="https://github.com/user-attachments/assets/ccda0e4d-0612-4036-97fd-2b9d6e51af61">
### JSON Semua Object
<img width="1273" alt="Screenshot 2024-09-17 at 13 38 35" src="https://github.com/user-attachments/assets/45d8174f-8e89-4b4d-8614-000badca09a3">
### XML search by ID
<img width="1270" alt="Screenshot 2024-09-17 at 13 38 51" src="https://github.com/user-attachments/assets/754c1f95-e743-4053-a016-414a689df143">
### JSON search by ID
<img width="1271" alt="Screenshot 2024-09-17 at 13 39 25" src="https://github.com/user-attachments/assets/0c9c1311-c61e-4088-863d-acebf0f2c4f6">

## Implementasi Checklist

1. Pertama, saya membuat sebuah template yang akan digunakan oleh template template lainnya. Hal ini dilakukan dengan cara membuat direktori baru di direktori utama proyek yang bernama `templates` lalu membuat sebuah file dengan nama `base.html`
2. Selanjutnya, saya isi `base.html` dengan boileprplate HTML dengan mengisi bagian `meta`  dengan ` {% block meta %} {% endblock meta %}` dan   `body` dengan `{% block content %} {% endblock content %}` untuk digunakan di template-template selanjutnya.
3. Agar `base.html` bisa dianggap sebagai template, saya menambahkan `[BASE_DIR/'templates']` pada setting `'DIRS'` yang ada di `settings.py` pada direktori project.
4. Setelah itu, saya mengubah isi dari `main.html` pada direktori `main/templates` agar `main.html` mengikuti base template yang sudah dibuat.
5. Untuk mengubah primary key setiap record dengan UUID, saya menambahkan 1 attribute pada `models.py` yang ada pada direktori `main` yaitu `id` yang menggunakan UUID sebagai value nya. id ini akan dibuat secara otomatis saat ada record baru yang ditambahkan ke database.
6. Untuk mengimplementasi perubahan yang dibuat, saya melakukan command:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
7. Selanjutnya, saya membuat form pertambahan makanan yang ada di file `forms.py` pada direktori `main` . Form ini meminta field-field sesuai dengan attribute yang dibutuhkan pada `models.py`.
8. Untuk mengaplikasikan form pada website, pertama saya menambahkan function `create_food_entry` pada file `views.py` pada `main` . function ini berisi logic untuk memeriksa kevalidasian form dan menyimpan object saat di input. Function ini akan menampilkan page form.
9. Di file yang sama, saya menambahkan `food_entries` yang mengambil semua object yang ada pada database untuk ditampilkan pada website.
10. pada `urls.py` yang ada pada direktori `main`, saya menambahkan path `create-food-entry` sebagai form untuk menginput data.
11. Untuk tampilan pada website, saya membuat template `create_food_entry.html` di direktori `templates` pada `main` yang akan menampilkan form dalam bentuk sebuah tabel.
12. Untuk mengimplementasi function `views.py` agar bisa menampilkan data dengan format XML atau JSON, saya menggunakan `serializers` untuk menampilkan data nya.
13. Pertama, saya membuat function `show_xml` yang mengambil seluruh data lalu menggunakan serializer untuk show dalam bentuk XML. Hal yang sama saya lakukan untuk `show_json` yang menampilkan JSON.
14. Untuk function search by id, saya membuat function `show_xml_by_id` dan `show_json_by_id` yang akan memfilter object berdasarkan ID.
15. Terakhir, saya menyambungkannya ke web dengan cara membuat path untuk masing-masing function yang sudah di buat.
