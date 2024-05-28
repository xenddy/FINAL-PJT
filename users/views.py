from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
    FollowSerializer,
)
from .models import Follow, User
from rest_framework.permissions import IsAuthenticated

class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get_object(self, username):
        return get_object_or_404(User, username=username)

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, username):
        password = request.data.get("password")
        password2 = request.data.get("password2")
        if (password or password2) and password != password2:
            return Response(
                {"error": "password or password2 not exist or password is not equal"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = self.get_object(username)
        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            if password:
                user.set_password(password)
                user.save()
            serializer = UserUpdateSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowToggleViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        follower = request.user
        username = kwargs.get('username')
        following = get_object_or_404(User, username=username)
        
        if follower == following:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        follow, created = Follow.objects.get_or_create(follower=follower, following=following)
        
        if not created:
            follow.delete()
            return Response({'detail': 'Unfollowed successfully.'}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({'detail': 'Followed successfully.'}, status=status.HTTP_201_CREATED)
