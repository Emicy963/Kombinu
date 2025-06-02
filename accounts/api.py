from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import UserProfile
from .serializers import (
    UserRegistrationSerializer, UserSerializer, UserProfileSerializer, LoginSerializer)

# Get the custom user model
User = get_user_model()

@extend_schema(
    summary='Registrar novo usuário',
    description='Cria uma nova conta de usuário e retorna os dados do usuário junto com o token de autenticação',
    responses={
        201: OpenApiResponse(
            response=UserSerializer,
            description='Usuário criado com sucesso',
            examples=[
                OpenApiExample(
                    'Sucesso',
                    value={
                        'user': {
                            'id': 1,
                            'username': 'joao123',
                            'email': 'joao@email.com',
                            'first_name': 'João',
                            'last_name': 'Silva',
                            'user_type': 'student'
                        },
                        'token': '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
                    }
                )
            ]
        ),
        400: OpenApiResponse(description='Dados inválidos')
    },
    tags=['Autenticação']
)

class RegisterView(generics.CreateAPIView):
    """View to handle user registration."""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        """Handle user registration and return auth token."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    
@extend_schema(
    summary='Login de usuário',
    description='Autentica um usuário existente e retorna o token de acesso',
    request=LoginSerializer,
    responses={
        200: OpenApiResponse(
            description='Login realizado com sucesso',
            examples=[
                OpenApiExample(
                    'Sucesso',
                    value={
                        'user': {
                            'id': 1,
                            'username': 'joao123',
                            'email': 'joao@email.com'
                        },
                        'token': '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
                    }
                )
            ]
        ),
        400: OpenApiResponse(description='Credenciais inválidas')
    },
    tags=['Autenticação']
)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Handle user login and return auth token."""
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'user': UserSerializer(user).data,
        'token': token.key
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    """Handle user logout by deleting the auth token."""
    try:
        request.user.auth_token.delete()
        return Response({'message': 'Logout realizado com sucesso.'}, status=status.HTTP_200_OK)
    except:
        return Response({'error': 'Erro ao realizar logout.'}, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(generics.RetrieveUpdateAPIView):
    """View to retrieve and update the user's profile."""
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        """Return the profile of the authenticated user."""
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile
