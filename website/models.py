from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the user model
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField()  # Field for the date
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  # Link to the author
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Field for featured image
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Link to category

    def __str__(self):
        return self.title
    
    
class Color(models.Model):
    color_code = models.CharField(max_length=7,default=None,blank=True,null=True)  # e.g., "#FFFFFF" for white
    color_image = models.ImageField(upload_to='color_images/')  # Directory for color images
    title = models.CharField(max_length=100)  # Name of the color

    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Product image (uploadable)
    description = models.TextField()   # Description of the product
    properties = CKEditor5Field('Properties')  # HTML data for properties using rich editor
    color_description = models.TextField(default="No color description available")   # Description of the product

    # Array fields for structured data, using JSONField
    range = CKEditor5Field('Range')   # Array of objects for product ranges
    technical_data = CKEditor5Field('Technical Data')   # Array of objects for technical data
    colors = models.ManyToManyField(Color, blank=True)
    def __str__(self):
        return self.name    
    
    
    
    
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = CKEditor5Field('Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()  # Field for the start date of the project
    end_date = models.DateField(null=True, blank=True)  # Optional field for the end date
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to the author
    featured_image = models.ImageField(upload_to='project_images/', null=True, blank=True)  # Field for featured image
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True)  # Link to project category

    def __str__(self):
        return self.title    