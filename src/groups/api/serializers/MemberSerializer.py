from rest_framework import serializers

from groups.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'user',
            'group',
            'reference',
            'balance',
            'open_tabs'
        )

    def to_representation(self, instance):
        self.Meta.depth = 1
        representation = super().to_representation(instance)
        self.Meta.depth = 0

        return representation
