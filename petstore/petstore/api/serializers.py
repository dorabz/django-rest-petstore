# created 

from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Pet, Tag, Category

class UserSerializer(serializers.ModelSerializer):
    pets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'pets', 'tags', 'categories']


class PetSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Pet
        fields = ['id', 'created', 'created_by', 'name', 'status', 'image', 'tags', 'category']


class TagSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    pets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'tag_name', 'created_by', 'pets']


class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    pets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'created_by', 'pets']
