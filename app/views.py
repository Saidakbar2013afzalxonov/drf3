from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# class PostView(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



@api_view(['GET'])
def PostList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PostView(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])
def PostCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({"message": "Ma'lumotlar noto'g'ri kiritildi!"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def PostUpdate(request, pk):
    post = Post.objects.get(pk=pk)

    serializer = PostSerializer(post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response({"message": "Postni yangilashda xatolik yuz berdi!"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def PostDelete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return Response({"message": "Post o'chirildi!"},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def PostListCreate(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"message": "Ma'lumotlar noto'g'ri kiritildi!"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def PostDetail(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({"message": "Postni to'liq yangilashda xatolik yuz berdi!"},status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({"message": "Postni qisman yangilashda xatolik yuz berdi!"},status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response({"message": "Post muvaffaqiyatli o'chirildi!"},status=status.HTTP_204_NO_CONTENT)