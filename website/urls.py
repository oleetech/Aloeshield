# blog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
from .views import ProjectViewSet, ProjectCategoryViewSet

from .views import ColorViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')  # Register BlogViewSet
router.register(r'projects', ProjectViewSet, basename='project')  # Register ProjectViewSet
router.register(r'project-categories', ProjectCategoryViewSet, basename='project-category')  # Register ProjectCategoryViewSet
router.register(r'colors', ColorViewSet)
router.register(r'products', ProductViewSet)
urlpatterns = [
    path('', include(router.urls)),  # Include all routes from the router
]
