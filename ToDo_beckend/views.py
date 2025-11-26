from .models import ToDo
from .serialziers import ToDoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class ToDoCrud(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]