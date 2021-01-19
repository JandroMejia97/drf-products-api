from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
