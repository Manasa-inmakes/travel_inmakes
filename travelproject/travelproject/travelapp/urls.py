from . import views
from django.urls import path

urlpatterns = [
    path('', views.myfun,name='myfun'),

    #path('add/',views.addition,name='addition'),
]