from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name="account"
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('', views.home, name="home-page"),
    path('members/', views.memList, name="mem-list"),
    path('donorform/', views.donateChildEdu, name="donate-child-education"),
    path('search/', views.search, name="search-mem"),
    path('upload/', views.upload, name="upload"),
    #path('upload_list/', views.upload_list, name="upload-list"),
    
    #path('upload/<int:pk>/', views.delete_photo, name="delete_photo"), 
    path('logout/', views.logout, name="logout"),
    path('/<int:pk>/', views.deletecreation, name='deletecreation'),

    
    
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
