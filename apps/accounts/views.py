from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserProfileSerializer, UserRegistrationSerializer

class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfuly.",
                "user_id": str(user.id),
                "email": user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        from django.contrib.auth import authenticate
        email = request.data.get("email")
        password = request.data.get("password")
        user_instance = authenticate(request, username=email, password=password)
        if user_instance is not None:
            refresh = RefreshToken.for_user(user_instance)
            user_serializer = UserProfileSerializer(user_instance)
            return Response({
                "access_token": str(refresh.acess_token),
                "refresh_token": str(refresh),
                "user": user_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
