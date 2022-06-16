from rest_framework import serializers
from .models import exampleApp

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = exampleApp
        fields = ('id', 'title', 'description', 'completed')