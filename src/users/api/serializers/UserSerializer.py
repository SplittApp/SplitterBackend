from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
            'password'
        )


    def to_representation(self, instance):
        self.Meta.depth = 1
        representation = super().to_representation(instance)
        self.Meta.depth = 0

        return representation
