from groups.models import Group
from groups.api.serializers.GroupSerializer import GroupSerializer
from rest_framework import viewsets

class GroupsViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
