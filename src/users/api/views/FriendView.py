from users.models import Friend
from users.api.serializers.FriendSerializer import FriendSerializer
from rest_framework import viewsets
from django.db.models import Q


class FriendViewSet(viewsets.ModelViewSet):
    serializer_class = FriendSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Friend.objects.filter(Q(friender__username=username) | Q(friended__username=username))
