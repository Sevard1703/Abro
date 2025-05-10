from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('about/', views.about),
    path('galery/', views.galery),
    path('politic/', views.politic),
    path('product/', views.product),
    path('smtp', views.smtp),
    path('parners', views.parners),
    path('contact', views.contact),
    path('beton', views.beton),
]  