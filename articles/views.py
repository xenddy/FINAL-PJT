from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Travel, Camping, Leisure, Cooking, Comments
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
    TravelSerializer, 
    CampingSerializer,
    LeisureSerializer,
    CookingSerializer,
    CommentsSerializer,
    LikeSerializer,
)

class BaseListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

class TravelList(BaseListView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class TravelDetail(BaseDetailView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class CampingList(BaseListView):
    queryset = Camping.objects.all()
    serializer_class = CampingSerializer

class CampingDetail(BaseDetailView):
    queryset = Camping.objects.all()
    serializer_class = CampingSerializer

class LeisureList(BaseListView):
    queryset = Leisure.objects.all()
    serializer_class = LeisureSerializer

class LeisureDetail(BaseDetailView):
    queryset = Leisure.objects.all()
    serializer_class = LeisureSerializer

class CookingList(BaseListView):
    queryset = Cooking.objects.all()
    serializer_class = CookingSerializer

class CookingDetail(BaseDetailView):
    queryset = Cooking.objects.all()
    serializer_class = CookingSerializer



class CommentsCreate(APIView):
    def post(self, request, model_name, object_id):

        model_name = model_name.lower()

        content_type = ContentType.objects.get(model=model_name)

        model_class = content_type.model_class()
        model_object = get_object_or_404(model_class, pk=object_id)
        
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save(content_object=model_object)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeCreate(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        article_id = request.data.get('article_id')
        article = get_object_or_404(Article, id=article_id)
        like, created = Like.objects.get_or_create(user=user, article=article)
        if not created:
            return Response({'detail': 'You already liked this article.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Article liked successfully.'}, status=status.HTTP_201_CREATED)

class LikeDelete(generics.DestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        article_id = request.data.get('article_id')
        article = get_object_or_404(Article, id=article_id)
        like = get_object_or_404(Like, user=user, article=article)
        like.delete()
        return Response({'detail': 'Like removed successfully.'}, status=status.HTTP_204_NO_CONTENT)
