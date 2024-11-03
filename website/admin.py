# blog/admin.py

from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Blog, Category,Product

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'date', 'author', 'featured_image', 'category']  # Add new fields here
        widgets = {
            'content': CKEditor5Widget(config_name='default'),  # Use CKEditor5Widget for content field
        }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm  # Use the BlogForm for the admin interface
    list_display = ('title', 'date', 'author', 'created_at', 'updated_at', 'category')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only set the author when creating a new object
            obj.author = request.user  # Set the author to the current user
        super().save_model(request, obj, form, change)    
        
        
from .models import Color
from django.utils.html import format_html

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_code', 'color_image')  # Show all relevant fields in list view
    search_fields = ('title', 'color_code')  # Allow searching by title and color code

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'description', 'properties', 'range', 'technical_data')  # Show all relevant fields
    search_fields = ('name', 'description')  # Allow searching by product name and description
    filter_horizontal = ('colors',)  # Enable multi-select for colors

    def image_preview(self, obj):
        """Displays a thumbnail of the product image in the list view."""
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: auto;" />', obj.image.url)
        return ""
    image_preview.short_description = "Image Preview"

    # To customize the form layout in the admin for product details
    # Organize fields into multiple fieldsets for better layout
    fieldsets = (
        ("Product Information", {
            'fields': ('name', 'image', 'description'),
            'description': "Basic details of the product."
        }),
        ("Properties", {
            'fields': ('properties',),
            'description': "Properties details of the product."
        }),
        ("Range", {
            'fields': ('range',),
            'description': "Range details of the product."
        }),
        ("Technical Data", {
            'fields': ('technical_data',),
            'description': "Technical specifications of the product."
        }),
        ("Color Information", {
            'fields': ('colors', 'color_description'),
            'description': "Color options and description of the product."
        }),
    )

    # Optional: Customize the form layout in the admin
    def get_form(self, request, obj=None, **kwargs):
        """Customize the form layout if needed."""
        form = super().get_form(request, obj, **kwargs)
        return form
    
    
    
from .models import Project, ProjectCategory
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'author', 'featured_image', 'category']  # Add new fields here
        widgets = {
            'description': CKEditor5Widget(config_name='default'),  # Use CKEditor5Widget for description field
        }
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the category name in the admin list view

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm  # Use the ProjectForm for the admin interface
    list_display = ('title', 'start_date', 'end_date', 'author', 'created_at', 'updated_at', 'category')  # Fields to display in the list view
    search_fields = ('title', 'description')  # Enable search by title and description
    ordering = ('-created_at',)  # Order projects by creation date, newest first

    def save_model(self, request, obj, form, change):
        if not change:  # Only set the author when creating a new object
            obj.author = request.user  # Set the author to the current user
        super().save_model(request, obj, form, change)  # Call the parent save_model method
    