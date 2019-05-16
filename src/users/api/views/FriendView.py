from users.models import Friend
from ..serializers import FriendSerializer
from rest_framework import viewsets

class FriendViewSet(viewsets.ModelViewSet):
    serializer_class = FriendSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Friend.objects.filter(Q(friender__user__username=username) | Q(friended__user__username=username))
