from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.serializers import ValidationError


from .serializers import UploadSerializer, UsersSerializer
from .models import Users

import pandas as pd



class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/list.html'

    def list(self, request):
        users_serializer = UsersSerializer(
            Users.objects.all(), many=True, context={'request': request, })
        response = {'users': users_serializer.data}
        return Response(response)

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')

        filedf = pd.read_csv(file_uploaded)

        for _, row in filedf.iterrows():
            userdata = row.to_dict()
            users_serializer = UsersSerializer(data=userdata)
            try:
                if users_serializer.is_valid(raise_exception=True):
                    users_serializer.save()
            except ValidationError as e:
                if (e.get_codes() == {'username': ['unique']}):
                    users_serializer.update(Users.objects.get(
                        username=row['username']), validated_data=userdata)

        users_serializer = UsersSerializer(
            Users.objects.all(), many=True, context={'request': request, })
        response = {'users': users_serializer.data}
        return Response(response)


class UsersViewSet(ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    