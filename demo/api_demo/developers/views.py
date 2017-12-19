from rest_framework.viewsets import ReadOnlyModelViewSet
from developers.models import Developers
from .serializers import DevSerializer
from .filters import DevFilter


class DevViewSet(ReadOnlyModelViewSet):
    queryset = Developers.objects.all()
    serializer_class = DevSerializer
    filter_class = DevFilter
