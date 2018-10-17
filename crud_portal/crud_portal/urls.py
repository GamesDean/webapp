"""crud_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import forms_builder.forms.urls

urlpatterns = [
    path('', include('firstapp.urls')), # come primo parametro se vuoto imposto la home, altrimenti il percorso es: post/
    path('admin/', admin.site.urls),
    path('forms/',include('forms_builder.forms.urls')), # per costruire i campi del DB in maniera dinamica

]
