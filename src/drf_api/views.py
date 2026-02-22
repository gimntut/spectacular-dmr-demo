from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

user_model = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = user_model
        fields = "__all__"


class UserViewSet(ModelViewSet):
    queryset = user_model.objects.all()
    serializer_class = UserSerializer
