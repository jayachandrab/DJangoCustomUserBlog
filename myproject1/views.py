from django.shortcuts import render
from operator import attrgetter
from blog.models import BlogPost
from django.views import View
from django.http import HttpResponse

# def home(request):
#     context={}
#     blog_posts=sorted(BlogPost.objects.all(),key=attrgetter('date_updated'),revers=True)
#     context['blog_posts']=blog_posts
#     return render(request,'ap1/home.html',context);


def about(request):
    context={'name':'jayachandra'}
    return render(request,'about.html',context);
class GreetingView(View):
    greeting = "Good Day"
    context={'greeting':greeting}
    def get(self, request):
        #context={'greeting':self.greeting}
        #return HttpResponse(self.greeting)
        self.context['greeting']=self.greeting

        return render(request,"about.html",context=self.context)
        



class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"
    context={}
    context['name']='jayachandra'
    #context['greeting']=greeting

