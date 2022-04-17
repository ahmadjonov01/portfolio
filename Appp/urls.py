from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
    path('photos/', views.photos, name='photos'),
    path('news/', views.news, name='news'),
    path('newsall/<int:id>', views.newsContent, name='newsall'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('aboutsingel/<int:id>', views.adoutsingel, name='aboutsingel'),
    path('base/', views.base, name='base'),]