from rest_framework import serializers

from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'synapse',
            'bio',
            'profile_pic',
            'facebook',
            'twitter'
        )

    def to_representation(self, instance):
        self.Meta.depth = 1
        representation = super().to_representation(instance)
        self.Meta.depth = 0

        return representation
