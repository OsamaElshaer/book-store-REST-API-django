from django.urls import path
from shop.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions



schema_view = get_schema_view(
   openapi.Info(
      title="Books Shop ",
      default_version='v1',
      description="RESTapi that contain all endpoints you will need it for books shop . ",
      contact=openapi.Contact(email="osamabinelshaer@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    path('swagger', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path("redoc", schema_view.with_ui('redoc',
                                    cache_timeout=0), name='schema-redoc'),
]