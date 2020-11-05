# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect


# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("Report:home")
#     context = {}
#     return render(request, 'registration/login.html', context)


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home');
    else:
        if request.method == 'POST':
            username = request.POST.get('username');
            password = request.POST.get('password');
            print('This is username: ', username);
			
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'registration/login.html', context)
