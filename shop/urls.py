from django.urls import path
from shop.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions





urlpatterns = [
    path('books/',BookView.as_view()),
    path('books-filter/',BookFilter.as_view()),
    path('favorites/',FavoriteView.as_view()),
    path('order/', OrderView.as_view()),
    path('cart/',CartView.as_view()),
    path('addtocart/', AddToCart.as_view()),
    path('delatecartbooks/', DelateCarBook.as_view()),
    path('deletecart/', DelateCart.as_view()),
    path('ordernow/', OrderCreate.as_view()),

]