from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,phone,password=None):
        if not email:
            raise ValueError("User must enter valid email")
        if not username:
            raise ValueError("User must enter username")
        if not phone:
            raise ValueError("User must enter valid phone number")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,phone,password):

        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            phone=phone,
            username=username,
            )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email=models.EmailField(verbose_name='email',max_length=50,unique=True)

    username=models.CharField(max_length=50,unique=True)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    phone=models.CharField(max_length=10)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username','phone']
    
    objects=MyAccountManager()
    
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)


    