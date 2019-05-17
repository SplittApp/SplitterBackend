from rest_framework import serializers

from users.models import Detail

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = (
            'id',
            'user',
            'gender',
            'phone',
            'street',
            'city',
            'state',
            'country',
            'zip_code'
        )


    def to_representation(self, instance):
        self.Meta.depth = 1
        representation = super().to_representation(instance)
        self.Meta.depth = 0

        return representation
