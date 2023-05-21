from . import views
from django.urls import path

urlpatterns = [
    path('babies', views.babies, name='babies'),
    path('products', views.products, name='products'),
    path('landscape', views.landscape, name='landscape'),
]