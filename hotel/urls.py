from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home,name="index"),
    path('contact/', views.contact),
    path('contactus/', views.contactus),
    path('home/', views.Home,name="home1")

]
