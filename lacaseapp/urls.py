from django.urls import path
from lacaseapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('checkout', views.checkout, name="checkout"),


    #
    path('fruits', views.fruits, name="fruits"),
    path('legumes', views.legumes, name="legumes"),
    path('corbeilles', views.corbeilles, name="corbeilles"),
    path('panier', views.panier, name="panier"),
    path('rgpd', views.rgpd, name="rgpd"),
    path('mentionLegale', views.mentionLegale, name="mentionLegale"),

    
]
