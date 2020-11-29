from django.urls import path, include
from Accounts import views

app_name = 'Accounts'

urlpatterns = [
    path('login/', views.loginPage, name='login'), 
]
