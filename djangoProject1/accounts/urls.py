from . import views
from django.urls import path


urlpatterns = [
    path('register.html/', views.register, name='register'),
    path('login.html/', views.login, name='login')
]