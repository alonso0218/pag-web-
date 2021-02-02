from django.contrib import admin
from django.urls import path

from webapp.views import home


urlpatterns = [
    path('',views.home,name="home"),
]