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



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Report:activity'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Report:activity'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'registration/login.html', {})