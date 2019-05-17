from groups.models import Group
from groups.api.serializers.GroupSerializer import GroupSerializer
from rest_framework import viewsets

class GroupsViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    lookup_field = 'reference'
    queryset = Group.objects.all()
    # def get_queryset(self):
    #     reference = self.kwargs['reference']
    #     return Group.objects.filter(reference=reference)
