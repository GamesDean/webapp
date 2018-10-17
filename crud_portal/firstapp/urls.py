#creata da me per collegarla alla root url

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
   

]
