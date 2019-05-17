from users.models import Detail
from users.api.serializers.DetailSerializer import DetailSerializer
from rest_framework import viewsets

class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    lookup_field = 'user__username'
    serializer_class = DetailSerializer
