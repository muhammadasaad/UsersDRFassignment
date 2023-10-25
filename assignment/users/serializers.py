from rest_framework.serializers import Serializer, HyperlinkedModelSerializer, FileField
from .models import Users

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']

class UsersSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields ='__all__'
    