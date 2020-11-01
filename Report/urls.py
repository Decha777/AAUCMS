from django.urls import path, include
from Report import views

app_name = 'Report'

urlpatterns = [
<<<<<<< HEAD
    path('tasks', views.list_activities, name='activity')
]
=======
    path('', views.list_activities, name='home'),
    path('tasks', views.list_activities, name='activity')
]

>>>>>>> main
