
from django.urls import path,include
from .views import home,about,index,MyFirstView,custom
from account.views import registration_view,loginView,logout_view,account_view,must_authenticate_view
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('',home,name="index"),
     path('home/',home, name='home'),
    path('register/',registration_view, name='register'),
    path('login/',loginView, name='login'),
    path('logout/',logout_view, name='logout'),
    path('must_authenticate/',must_authenticate_view,name='must_authenticate'),
   
    path('account/',account_view,name='account'),
     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
     path('mytemplates/',custom,name="mytemplates")


   
    
]
