from django.shortcuts import render, redirect
from lacaseapp.models import Contact, Product, OrderUpdate, Orders, Article
from django.contrib import messages
from math import ceil
from lacaseapp import keys
from django.conf import settings
MERCHANT_KEY=keys.MK
import json
from django.views.decorators.csrf import csrf_exempt
#from PayTm import Checksum

# Create your views here.
def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")


def fruits(request):
    tabfruits = []
    prod = Product.objects.filter(category = 2)
    n=len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    tabfruits.append([prod, range(1, nSlides), nSlides])

    params= {'tabfruits': tabfruits}
    
    return render(request, "fruits.html", params)

def legumes(request):
    
    legumes = []
    prod = Product.objects.filter(category = 1)
    n=len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    legumes.append([prod, range(1, nSlides), nSlides])
    params= {'legumes':legumes}
    return render(request, "legumes.html", params)

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

    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')
    
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json, name=name, amount=amount, state=state, zip_code=zip_code, phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id, update_desc="the order has been placed" )
        update.save()
        thank = True
# # PAYEMENT INTEGRATION
        id = Order.order_id
        oid=str(id)+"shopycart"
        param_dict = {

            'MID':keys.MID,
            'ORDER_ID' : oid,
            'TXN_AMOUNT' : str(amount),
            'CUST_ID' : email,
            'INDUSTRY_TYPE_ID' : 'Retail',
            'WEBSITE' : 'WEBSTAGING',
            'CHANNEL_ID' : 'WEB',
            'CALLBACK_URL' : 'http://127.0.0.1:8000/handllerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'checkout.html')



def panier(request):
    return render(request, "panier.html")

def corbeilles(request):
    return render(request, "corbeilles.html")


def mentionLegale(request):
    return render(request, "mentionLegale.html")

def rgpd(request):
    return render(request, "rgpd.html")
