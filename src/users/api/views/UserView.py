from django.contrib.auth.models import User
from users.api.serializers.UserSerializer import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.all() 
