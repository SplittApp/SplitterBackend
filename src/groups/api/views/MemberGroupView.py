from groups.models import Member
from groups.api.serializers.MemberSerializer import MemberSerializer
from rest_framework import viewsets

class MemberGroupViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    def get_queryset(self):
        reference = self.kwargs['reference']
        return Member.objects.filter(group__reference=reference)
