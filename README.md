# Repository Tugas PBP - Ezar Akhdan Shada Surahman
Markdown ini dibuat untuk memenuhi Tugas 2 PBP dengan nama aplikasi "Aina Homecook". 
Link Deployment PWS : http://ezar-akhdan-ainafnb.pbp.cs.ui.ac.id/
<details>

 <summary>Tugas 2 </summary>

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
<details>
<summary>Tugas 3</summary>

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
</details>
<details>
<summary>Tugas 4</summary>

### Perbedaan antara HttpResponseRedirect() dan redirect()
Perbedaan antara HttpResponseRedirect() dan redirect() terletak pada cara keduanya digunakan untuk melakukan redirect URL dan tingkat kontrol yang mereka tawarkan.

HttpResponseRedirect(): Mengembalikan respons HTTP 302 untuk mengarahkan ke URL yang ditentukan. Ini berguna saat Anda membutuhkan lebih banyak kontrol atas respons sebelum mengembalikannya, seperti ketika harus mengarahkan ke situs eksternal.
redirect(): Secara internal menggunakan HttpResponseRedirect(). Lebih praktis dan fleksibel karena dapat menerima berbagai jenis parameter, seperti URL, pola URL yang diberi nama, atau instance model.
Singkatnya, redirect() lebih sederhana dan fleksibel, sehingga lebih mudah digunakan dalam berbagai skenario. Sedangkan, HttpResponseRedirect() lebih baik digunakan ketika dibutuhkan kontrol lebih atas respons yang diberikan.

### Penghubungan model `food_entry` dengan `User`
Model `FoodEntry` terhubung ke model `User` melalui foreign key di `models.py`:
```
class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Ketika `FoodEntry` dibuat menggunakan fungsi `create_food_entry` (di `views.py`), entri tersebut terhubung dengan User yang sesuai.
```
def create_food_entry(request):
    form = FoodEntryForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        food_entry = form.save(commit=False)
        food_entry.user = request.user
        food_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_food_entry.html", context)
```

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Autentikasi adalah proses untuk memverifikasi identitas pengguna guna memastikan bahwa mereka adalah yang mereka klaim. Contohnya, dengan memasukkan username, password, atau OTP saat login. Dalam Django, autentikasi dilakukan menggunakan fungsi `authenticate()` dan `login()`.

Otorisasi berkaitan dengan menentukan tindakan atau sumber daya apa yang boleh diakses oleh pengguna setelah mereka diautentikasi. Di Django, otorisasi dikelola menggunakan permissions dan groups, serta dekorator seperti `@login_required` untuk mengontrol akses ke tampilan.

Ketika seorang pengguna login:
1. Menyediakan Kredensial: Pengguna mengirimkan username dan password.
2. Autentikasi: Sistem memverifikasi apakah kredensial cocok dengan data yang disimpan menggunakan fungsi `authenticate()` dari Django.
3. Pembuatan Sesi: Jika terautentikasi, Django membuat sesi untuk pengguna, menyimpan ID sesi sebagai cookie di browser.
4. Otorisasi: Sistem memeriksa permissions dan peran pengguna untuk menentukan sumber daya yang dapat diakses.
5. Redirect: Jika berhasil, pengguna diarahkan ke halaman tujuan.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang login melalui sesi yang disimpan dalam cookies. Ketika pengguna login, Django membuat sesi, menyimpan data sesi di server, dan memberikan ID sesi unik kepada pengguna. ID sesi ini dikirim ke browser pengguna sebagai cookie bernama sessionid. Setiap kali pengguna membuat permintaan baru, browser mengirim kembali cookie sessionid ke server, memungkinkan Django mengidentifikasi pengguna.

Cookies juga dapat digunakan untuk menyimpan preferensi pengguna, pelacakan, keranjang belanja dalam e-commerce, dan token keamanan. Namun, tidak semua cookies aman digunakan. Ada beberapa kekhawatiran terkait keamanan dan privasi. Cookies bisa rentan terhadap serangan seperti Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF) jika tidak dikelola dengan benar. Selain itu, cookies pelacakan dapat menimbulkan masalah privasi yang signifikan karena sering kali mengumpulkan data perilaku pengguna tanpa persetujuan eksplisit.

### Implementasi ceklist
1. Untuk mengimplementasikan register, login, dan sign up, beberapa function perlu di import:
    - `UserCreationForm` digunakan untuk mengimplementasikan fungsi registrasi.
    - `AuthenticationForm`, `authenticate`, dan `login` digunakan untuk mengimplementasikan fungsi login.
    - `logout` digunakan untuk mengimplementasikan fungsi logout.
    - `datetime`, `HttpResponseRedirect`, dan `reverse` digunakan untuk mengelola cookies.
2. Untuk mengaplikasikan cookies, beberapa perubahan perlu ditambahkan di function `show_main`:
```
...
context = {
        ...
        'last_login' : request.COOKIES['last_login']
    }
...
```
3. Saya membuat file `login.html` dan `register.html` pada direktori `main/templates` sebagai template untuk melakukan login dan register
4. Untuk mengimplementasikan logout, saya menambahkan sebuah button di dalam template `main.html`
5. Agar function-function baru tersebut bisa berjalan di aplikasi, perlu ditambahkan routing pada `urls.py`:
```
path('register/', register, name='register'),
path('login/', login_user, name="login"),
path('logout/', logout_user, name="logout"),
```
6. Untuk merestriksi halaman main dari user random, saya menggunakan decorator `@login_required` pada function `show_main` di `views.py`.
```
@login_required(login_url='login/')
```
7. Untuk mengubungkan `FoodEntry` yang sesuai untuk setiap user, saya menambah attribute pada `models.py`:
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
8. Setelah melakukan perubahan tersebut, tidak lupa untuk melakukan `makemigrations` dan `migrate` agar perubahan models teraplikasi.
9. Untuk menyimpan `FoodEntry` milik user dengan baik di database, perlu ditambahkan attribute user saat menyimpan form. Saya mengubah `create_food_entry`:
```
def create_food_entry(request):
    form = FoodEntryForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        food_entry = form.save(commit=False)
        food_entry.user = request.user
        food_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_food_entry.html", context)
```
9. Agar setiap user hanya bisa melihat `FoodEntry` milik masing-masing, saya merubah show main sehingga data yang diambil di-filter berdasarkan user yang terlogin:
```
@login_required(login_url='login/')
def show_main(request):
    food_entries = FoodEntry.objects.filter(user=request.user)
    context = {
        'name' : request.user.username,
        'food_entries': food_entries,
        'nama_aplikasi': "Aina Homecook",
        "nama_saya" : "Ezar Akhdan Shada Surahman",
        "kelas_saya" : "PBP B",
        'last_login' : request.COOKIES['last_login']
    }
    return render(request, "main.html", context)
```
### 2 User dan 3 Dummy data
1. User 1 dengan username chinese_food:
   <img width="1452" alt="Screenshot 2024-09-25 at 10 26 46" src="https://github.com/user-attachments/assets/404db717-4c6c-482a-94dd-bd586b49d260">

3. User 2 dengan username aina_dallas:
   <img width="1446" alt="Screenshot 2024-09-25 at 10 27 00" src="https://github.com/user-attachments/assets/4633d0b7-b460-463c-82a8-9ec36cdef52e">

</details>
<details>
<summary>Tugas 5</summary>

### Implementasi Checklist
1. Untuk menambah fitur edit dan delete menu, saya membuat 2 function baru pada direktori `main/views.py` yaitu function `edit_food` dan `delete_food`, berikut merupakan kedua functionnya:
```
def edit_food(request,id):
    food = FoodEntry.objects.get(pk=id)

    form = FoodEntryForm(request.POST or None, instance=food)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {
        'form' : form,
        'food' : food
        }
    return render(request, "edit_food.html" , context)

def delete_food(request,id):
    food = FoodEntry.objects.get(pk=id)
    food.delete()
    return HttpResponseRedirect(reverse("main:show_main"))
```
2. Selanjutnya, saya ingin membuat template untuk menampilkan view tersebut. Tapi sebelum itu, saya menghubungkan CDN Tailwind CSS ke file `base.html` di direktori `templates` pada root.
```
...
<script src="https://cdn.tailwindcss.com">
</script>
...
```
3. Setelah menghubungkan Tailwind, saya membuat file `edit_food.html` dan langsung styling dengan TailwindCSS. 
4. Agar terintegrasi dengan route website, saya menambahkan routing pada `urls.py` untuk kedua function ini.
```
...
    path('edit-food/<uuid:id>', edit_food, name="edit_food" ),
    path('delete-food/<uuid:id>', delete_food, name="delete_food")
...
```
5. Selanjutnya, agar bisa menggunakaan file image dan css global, saya membuat konfigurasi static files dengan membuat direktori `static` dan subdirektori `css` dan `image` untuk file-file yang dibutuhkan.
6. Setelah itu, saya mengkonfigurasi file settings.py dengan menambahkan baris ini pada `MIDDLEWARE`:
```
...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
]
...
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' # merujuk ke /static root project pada mode development
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
...
```
7. Saya juga menambahan file `global.css` pada direktori `static/css` dengan isi styling yang perlu dirubah dari.
8. Untuk bisa menggunakan static files yang telah dibuat, setiap template yang berhubungan tersebut harus menambahkan `{% load static %}` agar file static bisa digunakan.
9. Agar bisa me-reuse component yang dipakai berulang kali seperti navbar dan card, saya membuat component-component tersebut dalam template yang terpisah, lalu bisa saya panggil pada template lain dengan menggunakan `{% include '<nama-file>' %}`, yaitu `navbar.html` pada `templates` di direktori root, dan `card_food.html` serta `card_info.html` pada `main/templates`.
10. Terakhir, saya melakukan styling dengan TailwindCSS untuk file `create_food_entry.html`, `login.html`, `main.html`, dan `register.html` sampai mendapatkan layout dan design yang saya inginkan.

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. !important` akan mengesampingkan semua aturan kecuali yang lain juga menggunakan !important.
2. Inline styles (value = 1000)
3. ID selectors (value = 100) --> `#card {color: blue}`
4. Class, pseudo-class, attribute selectors, seperti .class, :hover, [type="text"]. (value = 10) --> `.form {color:green}`
5. Type selectors (value = 1) --> `p {color:black}`
6. Universal selector (value = 0)
Jika terdapat selector yang menggunakan gabungan dari beberapa jenis selector, maka selector dengan value terbesar akan diprioritaskan.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design sangat penting karena tidak semua user mengakses website dengan device yang memiliki ukuran yang sama. Ada yang mengakses dengan layar smartphone, ada juga yang mengakses dari layar desktop yang pastinya memiliki ukuran lebih besar. Jika design hanya disesuaikan untuk salah satu ukuran, maka user akan kesulitan untuk mengakses fitur-fitur website saat menggunakan ukuran yang berbeda.
- Aplikasi dengan design yang tidak responsif : Hampir tidak ada, salah satu contoh: https://dequeuniversity.com/library/responsive/1-non-responsive
- Aplikasi dengan design responsif : website SCELE Fasilkom UI

###  Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
1. Margin
Pengertian: Margin adalah ruang di luar elemen, antara elemen dengan elemen lain di sekitarnya. Margin digunakan untuk memberi jarak antar elemen.
Posisi: Margin berada di bagian paling luar dari elemen.
Pengaturan: Dapat diatur menggunakan margin-top, margin-right, margin-bottom, dan margin-left (atau shorthand margin untuk semua sisi).
2. Border
Pengertian: Border adalah garis yang mengelilingi elemen, di antara padding dan margin. Border bisa diatur ketebalannya, jenisnya (solid, dashed, dll.), serta warnanya.
Posisi: Border berada di antara margin dan padding.
Pengaturan: Dapat diatur menggunakan border-top, border-right, border-bottom, border-left, atau shorthand border.
3. Padding
Pengertian: Padding adalah ruang di dalam elemen, antara isi elemen (content) dengan border. Padding digunakan untuk memberi jarak antara konten dengan tepi elemen.
Posisi: Padding berada di antara konten elemen dan border.
Pengaturan: Dapat diatur menggunakan padding-top, padding-right, padding-bottom, dan padding-left (atau shorthand padding untuk semua sisi).

#### Perbandingan dan Ilustrasi
Jika kita membayangkan elemen sebagai sebuah kotak:
- Padding adalah ruang antara konten elemen dan garis tepi kotak.
- Border adalah garis tepi kotak.
- Margin adalah ruang di luar kotak, yang memisahkan elemen dari elemen lainnya.

### Flexbox dan Grid
**Flexbox** adalah sistem tata letak di CSS yang digunakan untuk mengatur elemen dalam satu arah, baik secara horizontal (baris) maupun vertikal (kolom). Flexbox memudahkan pemosisian dan distribusi elemen di dalam sebuah kontainer fleksibel, serta mendukung penyesuaian otomatis berdasarkan ukuran elemen. Dengan menggunakan properti seperti `justify-content`, `align-items`, dan `flex-wrap`, Flexbox memungkinkan pengaturan yang dinamis untuk elemen, seperti meratakan, memusatkan, atau mendistribusikan ruang secara seragam di dalam kontainer.

**Grid Layout** adalah sistem dua dimensi yang lebih kompleks dibandingkan Flexbox, yang memungkinkan pengaturan elemen dalam baris dan kolom. Grid sangat berguna untuk tata letak yang lebih terstruktur, di mana pengembang dapat mendefinisikan area grid dan posisi elemen dengan presisi. Properti seperti `grid-template-columns`, `grid-template-rows`, dan `grid-area` membantu membuat desain yang lebih grid-based dan simetris, ideal untuk tata letak halaman yang kompleks dengan beberapa elemen.

Keduanya memiliki kegunaan yang berbeda: Flexbox lebih baik untuk tata letak satu dimensi, seperti membuat navigasi horizontal atau kolom kartu produk, sementara Grid cocok untuk tata letak dua dimensi yang lebih kompleks, seperti desain halaman web dengan header, konten, dan sidebar yang harus diatur dalam area grid tertentu. Penggunaan keduanya memungkinkan fleksibilitas yang tinggi dalam desain web modern.
</details>