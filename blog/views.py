from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'blog/home.html')


def post_details(request, post_id):
    return render(request,'blog/post_details.html')
