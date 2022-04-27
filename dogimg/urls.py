from ast import Index
from unicodedata import name
from django.urls import path, include
from requests import post
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('predict', views.predict,name='predict')

    # 동익님
    # path('predict',views.predict,name='predict')

    # path('predict/', views.??????)

]