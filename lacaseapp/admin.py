from django.contrib import admin
from lacaseapp.models import Product, Categorie, Commande


# Register your models here.
admin.site.site_header ="La case à accras"
admin.site.site_title = "Boutiqque"
admin.site.index_title = "Administrateur"



class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added', 'description', 'image')
    search_fields = ('title',)
    list_editable = ('price', 'description', 'image',)

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'ville', 'pays', 'total', 'date_commande')

admin.site.register(Product, AdminProduct )
admin.site.register(Categorie, AdminCategorie )
admin.site.register(Commande, AdminCommande)

#admin.site.register(Contact )
#admin.site.register(Client )
#admin.site.register(Livreur )
#admin.site.register(Orders )
#admin.site.register(OrderUpdate )


