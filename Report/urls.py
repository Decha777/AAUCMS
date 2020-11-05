from django.urls import path, include
from Report import views
from django.views.generic import TemplateView

app_name = 'Report'

urlpatterns = [
    path('tasks', views.TaskView.as_view(), name='activity'),
    path('create_activity',views.create_activity),
    path('', views.report, name='home'),
]
