from groups.models import Member
from groups.api.serializers.MemberSerializer import MemberSerializer
from rest_framework import viewsets

class MembersViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
