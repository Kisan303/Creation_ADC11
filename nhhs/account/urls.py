from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('', views.home, name="home-page"),
    path('members/', views.memList, name="mem-list"),
    path('donorform/', views.donateChildEdu, name="donate-child-education"),
    path('search/', views.search, name="search-mem"),
    path('upload/', views.upload, name="upload"), 
    path('logout/', views.logout, name="logout"),

    
    
]
