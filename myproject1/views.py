from django.shortcuts import render
from operator import attrgetter
from blog.models import BlogPost

# def home(request):
#     context={}
#     blog_posts=sorted(BlogPost.objects.all(),key=attrgetter('date_updated'),revers=True)
#     context['blog_posts']=blog_posts
#     return render(request,'ap1/home.html',context);


def about(request):
    context={'name':'jayachandra'}
    return render(request,'about.html',context);
