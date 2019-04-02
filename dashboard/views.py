from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import BlogPost


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
    all_post=BlogPost.objects.all()
    context={
        'all_post':all_post
    }
    return render(request, 'dashboard/post_list.html',context)


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('post_title', None)
        description = request.POST.get('post_description', None)
        BlogPost.objects.create(title=title, details=description)
        return HttpResponseRedirect(reverse('post_list'))
    elif request.method == "GET":
        return render(request, 'dashboard/create_post.html')


@login_required
def update_post(request, post_id):
    return render(request, 'dashboard/update_post.html')


@login_required
def settings(request):
    return HttpResponse("Settings")
