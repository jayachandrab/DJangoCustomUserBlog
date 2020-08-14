from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from account.models import Account
from blog.models import BlogPost
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from blog.api.serializers import BlogPostSerializer
from rest_framework.filters import SearchFilter,OrderingFilter

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_detail_blog_view(request,slug):
    print("==========="+slug)
    try:
        b=BlogPost.objects.all()
        print(len(b))
        for blog in b:
            print(blog.slug)
        blog_post=BlogPost.objects.get(slug=slug)
        
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=BlogPostSerializer(blog_post)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def api_update_blog_view(request,slug):
    print("==========="+slug)
    try:
        b=BlogPost.objects.all()
        print(len(b))
        for blog in b:
            print(blog.slug)
        blog_post=BlogPost.objects.get(slug=slug)        
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user=request.user
    if blog_post.author!=user:
        return Response({'message':"you don't have permission to edit that post"})

    if request.method=='PUT':
        serializer=BlogPostSerializer(blog_post,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"]="Update Successful"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def api_delete_blog_view(request,slug):
    print("==========="+slug)
    try:
        b=BlogPost.objects.all()
        print(len(b))
        for blog in b:
            print(blog.slug)
        blog_post=BlogPost.objects.get(slug=slug)
        
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user=request.user
    if blog_post.author!=user:
        return Response({'message':"you don't have permission to delete that post"})
    if request.method=='DELETE':
        operation=blog_post.delete()
        data={}
        if operation:
            data['success']="delete success"
        else:
            data['failure']="delete failed"

        return Response(data=data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def api_create_blog_view(request):
    print("====== in create api")
    account=request.user
    #account=Account.objects.get(pk=1)
    blog_post=BlogPost(author=account)
    if request.method=="POST":
        serializer=BlogPostSerializer(blog_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ApiBlogListView(ListAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    pagination_class=PageNumberPagination
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('title','body','author__username')
    