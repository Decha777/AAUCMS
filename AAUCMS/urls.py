"""AAUCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
>>>>>>> dc4a1da56a331287e5e82cbe10a9775554ba22a1
from Report import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('Report.urls', namespace='report'))
=======
    path('tasks', views.list_activities)
>>>>>>> dc4a1da56a331287e5e82cbe10a9775554ba22a1
]
