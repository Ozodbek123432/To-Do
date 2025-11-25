from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout
from .serializer import UsersSerializers

class LoginAPIView(APIView):
    def post(self, request):
        serializer = UsersSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request, serializer.validated_data['user'])
        return Response({"msg": "Accaountingizga kirdingiz"})

class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"msg": "Accaountingizdan chiqdingiz"})