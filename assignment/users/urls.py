from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet, UsersViewSet

router = routers.DefaultRouter()
router.register('upload', UploadViewSet, basename="upload")
router.register('users', UsersViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    
]