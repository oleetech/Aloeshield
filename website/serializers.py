# blog/serializers.py

from rest_framework import serializers
from .models import Blog, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Show author name as string
    category = CategorySerializer()  # Nested category

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'date', 'author', 'featured_image', 'category']
        read_only_fields = ['author', 'created_at', 'updated_at']


from .models import Color

class ColorSerializer(serializers.ModelSerializer):
    color_image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = Color
        fields = ['color_code', 'color_image', 'title']
        
        
from .models import Project, ProjectCategory

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Show author name as string
    category = ProjectCategorySerializer()  # Nested category

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'author', 'featured_image', 'category']
        read_only_fields = ['author']        
        
        
from .models import Color, Product

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'color_code', 'color_image', 'title']


class ProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)  # Nested serializer to include color details

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'image', 'description', 'properties', 
            'color_description', 'range', 'technical_data', 'colors'
        ]