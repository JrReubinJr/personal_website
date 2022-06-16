from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExampleSerializer
from .models import exampleApp

# Create your views here.

class ExampleView(viewsets.ModelViewSet):
    serializer_class = ExampleSerializer
    queryset = exampleApp.objects.all()