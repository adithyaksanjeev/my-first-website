from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name="adithya_home"),
    path("about",views.a,name="adithya_about"),
    path("services",views.b,name="adithya_services")
]