from django.urls import path
#from lacaseapp import views
from lacaseapp.views import index, detail, rgpd, checkout, fruits, legumes, corbeilles, signup, login, confirmation, mentionLegale, contact, about, logout, register

urlpatterns = [
    path('', index, name="index"),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation"),

    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    #path('blog', views.blog, name="blog"),


    #
    path('signup', signup, name="signup"),
    path('register', register, name="register"),

    path('login', login, name="login"),
    path('logout', logout, name="logout"),


    path('fruits', fruits, name="fruits"),
    path('legumes', legumes, name="legumes"),
    path('corbeilles', corbeilles, name="corbeilles"),
    #path('panier', views.panier, name="panier"),
    path('rgpd', rgpd, name="rgpd"),
    path('mentionLegale', mentionLegale, name="mentionLegale"),

    
]
