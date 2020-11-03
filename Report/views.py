from django.shortcuts import render
from .models import Activity


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def list_activities(request):
    activities_list = Activity.objects.all()
    context = {'activities_list': activities_list}
    return render(request, '../templates/index.html', context)


# @login_required
def report(request):
    return render(request, '../templates/report.html')



