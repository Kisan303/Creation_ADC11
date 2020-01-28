from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('', views.index, name="home-page"),
    path('members/', views.memList, name="mem-list"),
    path('donate/', views.donateChildEdu, name="donate-child-education"),
    path('search/', views.search, name="search-mem"),

    
    
]