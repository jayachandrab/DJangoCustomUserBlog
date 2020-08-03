from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from account.forms import RegistrationForm,AccountAuthenticationForm,AccountUpdateForm

# Create your views here.

def registration_view(request):
    context={}
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            raw_password=form.cleaned_data.get('password1')
            account=authenticate(email=email,password=raw_password)
            login(request,account)
            return redirect('home')
        else:
            context['registration_form']=form
    else:
        form=RegistrationForm()
        context['registration_form']=form
    return render(request,'ap1/register.html',context)


def loginView(request):
    context={}
    user=request.user
    if user.is_authenticated:
        return redirect("home")
    if request.method=="POST":
        login_form=AccountAuthenticationForm(request.POST)
        if login_form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect('home')
    else:
        login_form=AccountAuthenticationForm()
    context['login_form']=login_form
    return render(request,'ap1/login.html',context)


def logout_view(request):
    logout(request)
    return redirect('home')

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context={}
  
    if request.method=="POST":
        account_form=AccountUpdateForm(request.POST,instance=request.user)
       
        if account_form.is_valid():
            account_form.initial={
                "email":request.POST['email'],
                "username":request.POST['username'],
                "phone":request.POST['phone']
            }

            account_form.save()
            context['success_message']="Profile Updated Successfully"

    else:
        
        account_form=AccountUpdateForm(
            initial={
                'email':request.user.email,
                'username':request.user.username,
                'phone':request.user.phone
            }
            )
       
    context['account_form']=account_form
    return render(request,'ap1/account.html',context)
