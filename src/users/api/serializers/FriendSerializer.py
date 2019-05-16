from rest_framework import serializers

from ..models import Friend

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = (
            'friender',
            'friended',
            'status',
            'blocked',
            'favorite',
        )
        depth=2
