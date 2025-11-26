from rest_framework import serializers
from ToDo_beckend.models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'