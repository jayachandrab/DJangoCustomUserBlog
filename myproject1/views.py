from django.shortcuts import render


def home(request):
    context={'name':'jayachandra'}
    return render(request,'home.html',context);


def about(request):
    context={'name':'jayachandra'}
    return render(request,'about.html',context);
