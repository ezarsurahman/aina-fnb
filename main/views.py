from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Ayam Kalasan',
        'price': 18000,
        'ready': "Ready",
        'description': "Ayam kremes diguyur sambel."
    }
    return render(request, "main.html", context)
