from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('booterms/', views.booterms, name='booterms')
]