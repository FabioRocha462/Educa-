from .serializer import MemorandoSerializer
from . models import Memorando
from rest_framework import viewsets

class MemorandoService(viewsets.ModelViewSet):
    
    queryset = Memorando.objects.filter(confirm = True)
    serializer_class = MemorandoSerializer