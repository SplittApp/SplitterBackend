from rest_framework import serializers

from users.models import Friend

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


    def to_representation(self, instance):
        self.Meta.depth = 1
        representation = super().to_representation(instance)
        self.Meta.depth = 0

        return representation
