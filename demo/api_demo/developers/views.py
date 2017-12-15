from rest_framework.viewsets import ModelViewSet
from developers.models import *
from .serializers import *


class DevViewSet(ModelViewSet):
    queryset = Developers.objects.all()
    serializer_class = DevSerializer

class EduViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EduSerializer

class SkViewSet(ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkSerializer

class EmpViewSet(ModelViewSet):
    queryset = Empl_history.objects.all()
    serializer_class = EmpSerializer
