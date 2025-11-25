from rest_framework import serializers
from ToDo_beckend.models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

class ToDoUserData(serializers.ModelSerializer):
    class Meta:
        model = ToDoUser
        fields = ['password', 'password1']

class PasswordReset(serializers.ModelSerializer):
    def passeord_reset(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Iltimos 8 ta dan koproq parol qoying")
        return password

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError("Parol bir xil emas")
        self.passeord_reset(attrs.get('password'))
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2", None)
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
