from django.shortcuts import render, redirect, get_object_or_404
from lacaseapp.models import Product, Commande
from django.contrib import messages
from math import ceil
from lacaseapp import keys
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
#from .form import UserForm, ProductForm
from django.contrib.auth.decorators import login_required



#from django.conf import settings


#MERCHANT_KEY=keys.MK
#import json
#import requests
#import datetime
#from django.views.decorators.csrf import csrf_exempt
#from PayTm import Checksum

# Create your views here.
#Meteo API
def index(request):
    product_objects = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_objects = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    #if 'city' in request.POST:
    #    city = request.POST['city']
    #else:
    #    city = 'Guadeloupe'
    #appid = 'cbe096d73a4354ebe22ae5f763d5ff10'
    #URL = 'http://api.openweathermap.org/data/2.5/weather'
    #PARAMS = {'q' : 'guadeloupe', 'appid': appid, 'units': 'metric'}
    #r = requests.get(url=URL, params=PARAMS)
    #res = r.json()
    #description = res['weather'][0]['description']
    #icon = res['weather'][0]['icon']
    #temp = res['main']['temp']
    #day = datetime.date.today()
    #{'description': description, 'icon': icon, 'temp':temp, 'day': day, 'city':city},
    return render(request, "shop/index.html",  {'product_objects' : product_objects})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, "shop/detail.html", {'product_object' : product_object})


def blog(request):
    return render(request, "blog.html")

def fruits(request):
    
    product_object = Product.objects.filter(category_id = 6)
    for e in product_object:
        print(e.category_id)

    print(product_object)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page) 
    return render(request, "shop/fruits.html",  {'product_object' : product_object})

def legumes(request):  
    product_object = Product.objects.filter(category_id = 7)
    for e in product_object:
        print(e.category_id)

    print(product_object)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, "shop/legumes.html",  {'product_object' : product_object})


def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name, email=email, desc=desc, phonenumber=pnumber)
        myquery.save()
        messages.info(request, "we will get back to you soon")
        return render(request, "contact.html")

    return render(request, "shop/contact.html")

def about(request):
    return render(request, "shop/about.html")

def checkout(request):
    if request.method=="POST":
        items = request.POST.get('items', '')
        total = request.POST.get('total', '')
        name = request.POST.get('nom', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        ville = request.POST.get('ville', '')
        pays = request.POST.get('pays', '')
        zipcode = request.POST.get('zipecode', '')
        com = Commande(name=name, email=email, address=address, pays=pays, ville=ville, zipcode=zipcode, items=items, total=total)
        com.save()
        return redirect('confirmation')
    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        name = item.name
    return render(request, "shop/confirmation.html", {'nom': name })

def corbeilles(request):
    return render(request, "corbeilles.html")


def mentionLegale(request):
    return render(request, "shop/mentionLegale.html")

def rgpd(request):
    return render(request, "shop/rgpd.html")

def register(request):
    #form = UserForm()
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        mon_utilisateur = User.objects.create_user(username, email, password)
        mon_utilisateur.first_name = firstname
        mon_utilisateur.last_name = lastname
        mon_utilisateur.save()
        messages.success(request, 'Votre compte à été créer avec success')
        return redirect('login')

    return render(request, 'app/register.html')


    return render(request, 'customadmin/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Bienvenu')
            return redirect('manage')
        else:
            messages.error(request, "error d'authentification")
        return redirect('login')

    return render(request, "customadmin/login.html")

@login_required
def deconnection(request):
    logout(request)



User = get_user_model()

def signup(request):
    if request.method == "POST":
        #Traiter le formulaire
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(email=email, username=username, password=password)

        login(request)
  
        return redirect("index")
    return render(request, "customadmin/signup.html")

#@login_required
#def productCreate(request):
#    form = ProductForm(request.POST or None)
#    messages = ''
#    if form.is_valid():
#        form.save()
#        form = ProductForm()
#        messages = "Vous avez reçu vos produits"
#    return render(request, "customadmin/create.html" , {'form' :form, 'message' :messages})

#@login_required
#def modifier(request, my_id):
#    obj = get_object_or_404(Product, id=my_id)
#    form = ProductForm(request.POST or None, isinstance=obj)
#    messages = ''
#    if form.is_valid():
#        form.save()
#        form = ProductForm()
#        messages = "Vos modifications ont été validé avec succès"
#    return render(request, "customadmin/create.html" , {'form' :form, 'message' :messages})

