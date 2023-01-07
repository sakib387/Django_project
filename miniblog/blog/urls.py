 
 

from django.contrib import admin
from django.urls import path
from . import views
 
 
urlpatterns = [
  #  path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('sinup/',views.user_sinup,name='sinup'),
    path('login/',views.user_login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('logout/',views.user_logout,name='logout'),
    path('addpost/',views.add_post,name='addpost'),
    path('updatepost/<int:id>/',views.update_post,name='update'),
    path('delete/<int:id>/',views.delete_post,name='delete'),
]
