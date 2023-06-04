from django.db import models

# Create your models here.
from django.urls import reverse


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)

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
    

class Cart(models.Model):
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart {self.id}"

    @property
    def total(self):
        return sum(item.subtotal for item in self.cart_items.all())

    def add_product(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        cart_item.quantity += quantity
        cart_item.save()

    def remove_product(self, product):
        cart_item = CartItem.objects.get(cart=self, product=product)
        cart_item.delete()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def subtotal(self):
        return self.product.price * self.quantity
    
#Models category-Blog
class CategoryBlog(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, unique=True)
def __str__(self):
        return self.name 

def get_absolute_url(self):
        return reverse('article', args=[self.id, self.slug])

class Article(models.Model):
    article_id = models.AutoField
    article_name = models.CharField(max_length=200, db_index=True)
    stock = models.IntegerField(default=0.0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='article/%Y/%d', blank=True, null=True)
    Category = models.ForeignKey(Category, 
    related_name='article', on_delete=models.CASCADE, max_length=200, default="", )
    slug = models.CharField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ('name',)
        index_together = (('id', 'slug'),)

    def  __str__(self):
        return self.article_name

    def get_absolute_url(self):
        return reverse('article', args=[self.id, self.slug])

