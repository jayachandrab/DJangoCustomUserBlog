from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import authenticate,login
from account.models import Account
from django.views.generic.base import ContextMixin 
from django.views.generic import TemplateView 
from django.template.loader import render_to_string
from operator import attrgetter
from blog.models import BlogPost
from blog.views import get_blog_queryset
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


BLOG_POSTS_PER_PAGE=1

def custom(request):
    rendered = render_to_string('ap1/custom.html', {'foo': 'custom2.html'})
    return render(request,rendered)


class BaseContextMixin(ContextMixin):
    
    def get_context_data(self, **kwargs):
        context_data = super(BaseContextMixin, self).get_context_data(**kwargs)
        common_data_1 = ...
        context_data["common_key_1"] = 'common_data_1'
        common_data_2 = ...
        context_data["common_key_2"] = 'common_data_2'
        ...
        return context_data
    
class MyFirstView(TemplateView, BaseContextMixin):
    template_name = "ap1/my_first_template.html"
    #rendered = render_to_string('my_template.html', {'foo': 'bar'})

    def get_context_data(self, **kwargs):
        context_data = super(MyFirstView, self).get_context_data(**kwargs)
        context_data["my_special_key"] = 'hello 1'
        return context_data

class MySecondView(TemplateView, BaseContextMixin):
    template_name = "ap1/my_second_template.html"

    def get_context_data(self, **kwargs):
        context_data = super(MySecondView, self).get_context_data(**kwargs)
        context_data["my_special_key_2"] = 'my_special_data_2'
        return context_data

def index(request):

    return render(request,'ap1/index.html')


def home(request):
    query=""
    context={}
    if request.GET:
        query=request.GET.get('q','')
        context['query']=str(query)

    blog_posts=sorted(get_blog_queryset(query),key=attrgetter('date_updated'),reverse=True)

    

    #Pagination

    page=request.GET.get('page',1)
    blog_post_paginator=Paginator(blog_posts,BLOG_POSTS_PER_PAGE)


    try:
        blog_posts=blog_post_paginator.page(page)
    except PageNotAnInteger:
        blog_posts=blog_post_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts=blog_post_paginator.page(blog_post_paginator.num_pages )

    context['blog_posts']=blog_posts
   
    return render(request,'ap1/home.html',context);


# def register(request):   
#     print("======== register")
#     if request.method=='POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']

#             user=authenticate(username=username,password=password)
#             login(request,user)
#             return redirect('index')
#     form=UserCreationForm()
#     context={'form':form}
#     return render(request,'registration/register.html',context);


def about(request):
    return render(request,'ap1/about.html')
