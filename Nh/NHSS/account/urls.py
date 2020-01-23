
from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),

]
