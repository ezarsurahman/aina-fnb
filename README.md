# Tugas 2 PBP - Ezar Akhdan Shada Surahman

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

### Git dan PWS Deploymeny

20. Saya membuat repository baru di github lalu menghubungkannya kepada repository yang ada pada lokal (melakukan `git init` terlebih dahulu)
21. Setelah terhubung, saya melakukan `add`, `commit`, dan `push` ke remote repository github
22. Untuk melakukan deployment ke PWS, pertama saya menambahkan URL repo saya ke list `ALLOWED_HOST` pada `settings.py`.
23. Terakhir, saya menyambungkan repository dengan PWS, lalu melakukan push ke repository PWS untuk melakukan deployment.
