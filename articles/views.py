from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Comment,Article,Like
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
    CommentSerializer,ArticleSerializer,
)

class BaseListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.is_authenticated:
                serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

class TravelList(BaseListView):
    queryset = Article.objects.filter(category = 'Travel')
    serializer_class = ArticleSerializer

class TravelDetail(BaseDetailView):
    queryset = Article.objects.filter(category = 'Travel')
    serializer_class = ArticleSerializer

class CampingList(BaseListView):
    queryset = Article.objects.filter(category = 'Camping')
    serializer_class = ArticleSerializer

class CampingDetail(BaseDetailView):
    queryset = Article.objects.filter(category = 'Camping')
    serializer_class = ArticleSerializer

class LeisureList(BaseListView):
    queryset = Article.objects.filter(category = 'Leisure')
    serializer_class = ArticleSerializer

class LeisureDetail(BaseDetailView):
    queryset = Article.objects.filter(category = 'Leisure')
    serializer_class = ArticleSerializer

class CookingList(BaseListView):
    queryset = Article.objects.filter(category = 'Cooking')
    serializer_class = ArticleSerializer

class CookingDetail(BaseDetailView):
    queryset = Article.objects.filter(category = 'Cooking')
    serializer_class = ArticleSerializer



class CommentGetPost(APIView):
    def get(self, request, Article_pk):
        Article = Article.objects.get(id=Article_pk)
        comments = Article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    def post(self, request,Article_pk):
        Article = Article.objects.get(id=Article_pk)
        if not request.user.is_authenticated:
            return Response(
                {"error": "인증이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = CommentSerializer(data=request.data, context={"view": self})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentPutDelete(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)
    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        if comment.user != request.user and not request.user.is_superuser:
            return Response(
                {"error": "작성자만 수정할 수 있습니다."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        if comment.user != request.user and not request.user.is_superuser:
            return Response(
                {"error": "작성자만 삭제할 수 있습니다."},
                status=status.HTTP_403_FORBIDDEN,
            )
        comment.delete()
        data = {"delete": f"댓글 ({comment_pk})번이 삭제되었습니다."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)

class LikeCreate(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request,article_id):
        user = request.user
        # article_id = request.data.get('article_id')
        article = get_object_or_404(Article, id=article_id)
        like, created = Like.objects.get_or_create(user=user, article=article)
        if not created:
            return Response({'detail': 'You already liked this article.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Article liked successfully.'}, status=status.HTTP_201_CREATED)

    def delete(self, request,article_id):
        user = request.user
        # article_id = request.data.get('article_id')
        article = get_object_or_404(Article, id=article_id)
        like = get_object_or_404(Like, user=user, article=article)
        like.delete()
        return Response({'detail': 'Like removed successfully.'}, status=status.HTTP_204_NO_CONTENT)
