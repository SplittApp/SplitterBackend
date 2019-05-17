from groups.models import Group
from groups.api.serializers.GroupSerializer import GroupSerializer
from rest_framework import viewsets

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    def get_queryset(self):
        reference = self.kwargs['reference']
        return Group.objects.filter(reference=reference)
