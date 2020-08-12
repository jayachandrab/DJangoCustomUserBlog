from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def registration_view(request):
    print("=====in register api=====")
    if request.method == 'POST':
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']="Successfully registered a new user."
            data['email']=account.email
            data['username']=account.username
            token=Token.objects.get(user=account).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data)