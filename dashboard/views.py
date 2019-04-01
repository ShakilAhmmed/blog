from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user_authenticate = authenticate(username=username, password=password)
        if user_authenticate is not None:
            login(request, user_authenticate)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('login'))
    elif request.method == 'GET':
        return render(request, 'dashboard/login.html')


@login_required
def admin_logout(request):
    logout(request)
    context = {
        'message': "You're Logged Out Successfully"
    }
    return render(request, 'dashboard/login.html', context)


@login_required
def home(request):
    return render(request, 'dashboard/admin_home.html')


@login_required
def post_list(request):
    return render(request, 'dashboard/post_list.html')


@login_required
def create_post(request):
    return render(request, 'dashboard/create_post.html')


@login_required
def update_post(request, post_id):
    return render(request, 'dashboard/update_post.html')


@login_required
def settings(request):
    return HttpResponse("Settings")
