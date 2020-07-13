from django.db.models import Q
from rest_framework import status
from api.models import Author, Post
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .serializers import AuthorSerializer, PostSerializer


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)

        if request.method == 'GET':
            author_serializer = AuthorSerializer(author)
            return JsonResponse(author_serializer.data)

        elif request.method == 'PUT':
            author_data = JSONParser().parse(request)
            author_serializer = AuthorSerializer(author, data=author_data)
            if author_serializer.is_valid():
                author_serializer.save()
                return JsonResponse(author_serializer.data)
            return JsonResponse(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            author.delete()
            return JsonResponse({'message': 'Author was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'The author does not exists'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def news_list(request):
    search = request.GET.get('filter', None)

    if search:
        news = Post.objects.filter(Q(title__contains=search) | Q(text__contains=search))
        serializer = PostSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'GET':
        news = Post.objects.all()
        serializer = PostSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def news_detail(request, pk):
    try:
        new = Post.objects.get(pk=pk)

        if request.method == 'GET':
            new_serializer = PostSerializer(new)
            return JsonResponse(new_serializer.data)

        elif request.method == 'PUT':
            author_data = JSONParser().parse(request)
            new_serializer = PostSerializer(new, data=author_data)
            if new_serializer.is_valid():
                new_serializer.save()
                return JsonResponse(new_serializer.data)
            return JsonResponse(new_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            new.delete()
            return JsonResponse({'message': 'News was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'The news does not exists'}, status=status.HTTP_404_NOT_FOUND)
