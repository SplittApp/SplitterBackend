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
        depth=2
