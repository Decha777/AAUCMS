from django.urls import path, include
from Report import views

app_name = 'Report'

urlpatterns = [
    path('tasks', views.list_activities, name='activity')
]
