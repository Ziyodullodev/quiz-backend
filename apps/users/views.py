from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response(
                {
                    "error": "Please provide both username and password"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {
                    "error": "Invalid Credentials"
                }, status=status.HTTP_404_NOT_FOUND
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": str(token),
                "user": UserSerializer(user).data,
            }, status=status.HTTP_200_OK
        )


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.get_or_create(user=serializer.instance)
            return Response(
                {
                    "status": "success",
                    "user": serializer.data,
                    "token": str(token[0]),
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "status": "error",
                "errors": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST
        )
    

class UpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "user": serializer.data,
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                "status": "error",
                "errors": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST
        )
    
