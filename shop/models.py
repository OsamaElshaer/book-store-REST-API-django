from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.title

    

class Book(models.Model):
    title = models.CharField(max_length=100,)
    data = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True,blank=True)
    image = models.ImageField(upload_to="books/",null=True,blank=True)
    marcket_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200,null=True,blank=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
        

    def __str__(self):
        return self.title
        


class Favorite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.Case)
    isFavorite = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['book']
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return f"BookID ={self.book.id}user={self.user.username}|ISFavorite={self.isFavorit}"



class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    isComplete = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User={self.user.username}|ISComplete={self.isComplete}"



class CartBook(models.Model):
    cart = models.ForeignKey(Payment, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart=={self.cart.id}<==>Cartbook:{self.id}==Qualtity=={self.quantity}"


class Order(models.Model):
    cart = models.OneToOneField(Payment, on_delete=models.CASCADE)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['updated']


    def __str__(self):
        return self.cart.user
        
