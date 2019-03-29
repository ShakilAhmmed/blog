from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'dashboard/admin_home.html')
    #return HttpResponse("This is Home")


def login(request):
    return render(request,'dashboard/login.html')


def post_list(request):
    return render(request,'dashboard/post_list.html')


def create_post(request):
    return render(request,'dashboard/create_post.html')


def update_post(request, post_id):
    return render(request, 'dashboard/update_post.html')


def settings(request):
    return HttpResponse("Settings")
