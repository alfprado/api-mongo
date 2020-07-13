from .models import News, Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'text', 'author', 'created_date']



