from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('meni/', views.meni, name='meni'),
    path('onama/', views.onama, name='onama'),
    path('kontakt/', views.kontakt, name='kontakt'),
]

urlpatterns += staticfiles_urlpatterns()