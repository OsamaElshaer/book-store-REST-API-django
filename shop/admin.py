from shop.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Payment)
admin.site.register(CartBook)
admin.site.register(Order)

