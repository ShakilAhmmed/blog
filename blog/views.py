from django.http import HttpResponse
from django.shortcuts import render
from dashboard.models import BlogPost


# Create your views here.
def home(request):
    all_post = BlogPost.objects.all()
    total_posts=all_post.count()
    context={
        'all_post':all_post,
        'total_posts':total_posts
    }
    return render(request, 'blog/home.html',context)


def post_details(request, post_id):
    single_post=BlogPost.objects.filter(pk=post_id)
    print(single_post)
    context={
        'single_post':single_post
    }
    return render(request, 'blog/post_details.html',context)
