from groups.models import Member
from groups.api.serializers.MemberSerializer import MemberSerializer
from rest_framework import viewsets

class MemberUserViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Member.objects.filter(user__username=username)
