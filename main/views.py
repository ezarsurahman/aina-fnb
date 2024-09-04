from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Ayam Kalasan',
        'price': 18000,
        'ready': "Ready",
        'description': "Ayam kremes dengan baluran sambal.",
        'nama_aplikasi': "Aina Homecook",
        "nama_saya" : "Ezar Akhdan Shada Surahman",
        "kelas_saya" : "PBP B"
    }
    return render(request, "main.html", context)
    