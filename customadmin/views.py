from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, admin_login
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        #Traiter le formulaire
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user.object.create_user(email=email, username=username, password=password)

        login(request, user)
  
        return redirect("index")
    return render(request, "customadmin/signup.html")
#def admin_login(request):
    #try: 
    #    if request.user.is_authentificated:
    #        return redirect('/dashboard/')
    #    # messages.info(request, 'Account not found')
    #    if request.method == 'POST':
    #        username = request.POST.get('username')
    #        password = request.POST.get('password')
    #        user_obj = User.objects.filter(username = username)
    #        if not user_obj.exists ():
    #            messages.info(request, 'Account not found')
    #            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #        user_obj = authenticate(username = username, password = password)
#
    #        if user_obj and user_obj.is_superuser: 
    #            login(request, user_obj)
    #            return redirect('/dashboard/')
    #        
    #        messages.info(request, 'invalid password')
    #        return redirect('/')
    #    
    #    return render(request, 'shop/signup.html')
    #except Exception as e: 
    #    print(e)

#def dashboard(request):
#    return render(request, 'dashboard.html')
#
#def amenities(request):
#    objs = amenities.objects.all()
#    return render(request, 'dashboard.html', {'objs': objs})