from django.contrib.auth import authenticate
from rest_framework import serializers
class UsersSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Login yoki parol xato')
        data['user'] = user
        return data