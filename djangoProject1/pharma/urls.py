from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path('register.html/', views.registerPage, name = 'register'),
    path('login.html/', views.loginpage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('', views.homeview.as_view(), name='home'),
    path('about.html/',views.about, name='about'),
    path('shop.html/', views.shop, name='shop'),
    path('<int:pk>/', views.itemdetailview.as_view(), name='shop-single'),
    path('cart.html/', views.cart, name= 'cart'),
    path('checkout.html/', views.checkout, name='check'),
    path('update_item/', views.updateItem, name='checkout')
]