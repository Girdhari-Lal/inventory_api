from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from users.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated 

# Utility function to generate JWT tokens for a given user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Accepts user data, validates it, creates a new user, and returns JWT token
# http://127.0.0.1:8000/register/
class UserRegisterView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response({
            'Message': 'User not created',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

# Authenticates user credentials and returns JWT tokens if valid
# http://127.0.0.1:8000/login/
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email = email, password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'Message': 'Login Success'}, status = status.HTTP_200_OK)
            else:
                return Response({'Error' : 'Email or password is not valid'}, status = status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#Returns the profile information of the currently authenticated user
# http://127.0.0.1:8000/user/
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user:
            return Response(
                {"error": "User is not authenticated"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)