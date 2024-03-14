from django.shortcuts import render
from rest_framework import generics
from ducks.models import Duck
from ducks.serializers import DuckSerializer

class DuckListAPIView(generics.ListAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer
# Create your views here.
class DuckDetailAPIView(generics.RetrieveAPIView): 
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer