from django.shortcuts import render
from .models import Activity

# Create your views here.
def list_activities(request):
    activities_list = Activity.objects.all()
    context = {'activities_list': activities_list}
    return render(request, '../templates/index.html', context)