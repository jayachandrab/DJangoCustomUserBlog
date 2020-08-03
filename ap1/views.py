from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import authenticate,login
from account.models import Account

def index(request):

    return render(request,'ap1/index.html')


def home(request):
    context={}
    accounts=Account.objects.all()
    context['accounts']=accounts
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
