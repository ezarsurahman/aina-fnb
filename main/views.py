import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib import messages
from main.models import FoodEntry
from main.forms import FoodEntryForm
@login_required(login_url='login/')
def show_main(request):
    
    context = {
        'name' : request.user.username,
        'nama_aplikasi': "Aina Homecook",
        "nama_saya" : "Ezar Akhdan Shada Surahman",
        "kelas_saya" : "PBP B",
        "npm" : "2306165894",
        'last_login' : request.COOKIES['last_login']
    }
    return render(request, "main.html", context)

def create_food_entry(request):
    form = FoodEntryForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        food_entry = form.save(commit=False)
        food_entry.user = request.user
        food_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_food_entry.html", context)

def show_xml(request):
    data = FoodEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = FoodEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = FoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = FoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if(form.is_valid()):
            user = form.get_user()
            login(request,user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            date_now = datetime.datetime.now()
            date_formatted = date_now.strftime("%a %B %Y - %H:%I:%M")
            response.set_cookie('last_login',date_formatted)
            return response
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm
    context = {'form':form}
    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

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

@csrf_exempt
@require_POST
def add_food_entry_ajax(request):
    img = request.POST.get("img")
    name = request.POST.get("name")
    price = request.POST.get("price")
    ready = request.POST.get("ready")
    description = request.POST.get("description")

    new_food = FoodEntry(
        img=img, name=name,
        price=price, ready=ready,
        description=description, user=request.user
    )
    new_food.save()
    return HttpResponse(b"CREATED",status=201)