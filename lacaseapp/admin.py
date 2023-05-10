from django.contrib import admin

# Register your models here.
from lacaseapp.models import Product, Category, Client, Livreur, Contact, Orders, OrderUpdate


admin.site.register(Contact )
admin.site.register(Product )
admin.site.register(Category )
admin.site.register(Client )
admin.site.register(Livreur )
admin.site.register(Orders )
admin.site.register(OrderUpdate )


