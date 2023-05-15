from django.db import models

# Create your models here.
from django.urls import reverse


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)
    #phonenumber=models.ImageField()

    def __int__(self):
        return self.id


class Client(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    prenoms = models.CharField(max_length=200, db_index=True)
    date_de_naissance = models.CharField(max_length=200, db_index=True)
    date_inscription = models.CharField(max_length=200, db_index=True)
    postal_addresse = models.CharField(max_length=200, db_index=True)
    email = models.CharField(max_length=200, db_index=True)
    password = models.CharField(max_length=50)


class Livreur(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    prenoms = models.CharField(max_length=200, db_index=True)
    date_de_naissance = models.CharField(max_length=200, db_index=True)
    date_inscription = models.CharField(max_length=200, db_index=True)
    postal_addresse = models.CharField(max_length=200, db_index=True)
    adresse_facturation = models.CharField(max_length=200)
    email = models.CharField(max_length=200, db_index=True)
    password = models.CharField(max_length=50)

class Login(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    prenoms = models.CharField(max_length=200, db_index=True)
    email = models.CharField(max_length=200, db_index=True)

#Models category produits.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, unique=True)

    #class Meta:
    #    ordering = ('name',)
    #    verdose_name = 'category'
    #    verdose_name_plural = 'categories'
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        #return reverse('product', kwargs={"slug" : self.slug})
        return reverse('product', args=[self.id, self.slug])


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0.0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%d', blank=True, null=True)
    category = models.ForeignKey(Category, 
    related_name='products', on_delete=models.CASCADE, max_length=200, default="", )
    slug = models.CharField(max_length=200, db_index=True)
    #image = models.ImageField(upload_to='images/images')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ('name',)
        index_together = (('id', 'slug'),)

    def  __str__(self):
        return self.product_name

    def get_absolute_url(self):
        #return reverse('product', kwargs={"slug" : self.slug})
        return reverse('product', args=[self.id, self.slug])

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    adress1 = models.CharField(max_length=200)
    adress2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    oid = models.CharField(max_length=150, blank=True)
    amountpaid = models.CharField(max_length=500, blank=True, null=True)
    paymentstatus = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."