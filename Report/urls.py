from django.urls import path, include
from Report import views
from django.views.generic import TemplateView

app_name = 'Report'

urlpatterns = [
    path('tasks', views.TaskView.as_view(), name='activity'),
    path('create_activity',views.create_activity),
    path('', views.report, name='home'),
    path('get_decision_name',views.get_decision_name),
    path('get_problem_name',views.get_problem_name),
    path('get_responsible_person',views.get_responsible_person),
    path('get_activities_task',views.get_activities_task),

]
