from .serializer import MemorandoSerializer, OfficialSerializer, RequerimentSerializer
from . models import Memorando, Official, Requeriment
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.urls import get_urlconf




class MemorandoService(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Memorando.objects.filter(confirm = True).order_by('created_at')
        serializer = MemorandoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = Memorando.objects.filter(confirm = True)
        memorando = get_object_or_404(queryset, pk=pk)
        serializer = MemorandoSerializer(memorando)
        return Response(serializer.data)

class OfficialService(viewsets.ViewSet):

    def list(self, request):
        queryset = Official.objects.filter(confirm = True).order_by('created_at')
        serializer = OfficialSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = Official.objects.filter(confirm = True)
        offcial = get_object_or_404(queryset, pk=pk)
        serializer = OfficialSerializer(offcial)
        return Response(serializer.data)

class RequerementService(viewsets.ViewSet):

    def list(self, request):
        queryset = Requeriment.objects.filter(confirm = True).order_by('created_at')
        serializer = RequerimentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = Requeriment.objects.filter(confirm = True)
        requeriment = get_object_or_404(queryset, pk=pk)
        serializer = RequerimentSerializer(requeriment)
        return Response(serializer.data)

