from rest_framework import generics, status
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Comment,Article,Like
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
    CommentSerializer,ArticleSerializer,
)
from django.http import HttpResponseRedirect
from django.urls import reverse

class BaseListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class TravelList(BaseListView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(category='Travel')
        serializer = ArticleSerializer(articles, many=True)
        return render(request, 'Travel.html', {'articles': serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            new_article_id = serializer.data.get('id')
            return redirect('articles:Travel_detail', pk=new_article_id)  # 여기에서 패턴 이름을 수정
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_new_post_page(cls, request):
        return render(request, 'newlist.html')

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(category='Travel')
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # 댓글을 가져오는 부분 추가
        comments = instance.comments.all()
        comment_serializer = CommentSerializer(comments, many=True)

        return render(request, 'Travel_detail.html', {'article': serializer.data, 'comments': comment_serializer.data})

class CampingList(BaseListView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(category='Camping')
        serializer = ArticleSerializer(articles, many=True)
        return render(request, 'Camping.html', {'articles': serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            new_article_id = serializer.data.get('id')
            return redirect('articles:Camping_detail', pk=new_article_id)  # 여기에서 패턴 이름을 수정
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_new_post_page(cls, request):
        return render(request, 'newlist.html')

class CampingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(category='Camping')
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # 댓글을 가져오는 부분 추가
        comments = instance.comments.all()
        comment_serializer = CommentSerializer(comments, many=True)

        return render(request, 'Camping_detail.html', {'article': serializer.data, 'comments': comment_serializer.data})

class LeisureList(BaseListView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(category='Leisure')
        serializer = ArticleSerializer(articles, many=True)
        return render(request, 'Leisure.html', {'articles': serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            new_article_id = serializer.data.get('id')
            return redirect('articles:Leisure_detail', pk=new_article_id)  # 여기에서 패턴 이름을 수정
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_new_post_page(cls, request):
        return render(request, 'newlist.html')

class LeisureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(category='Leisure')
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # 댓글을 가져오는 부분 추가
        comments = instance.comments.all()
        comment_serializer = CommentSerializer(comments, many=True)

        return render(request, 'Leisure_detail.html', {'article': serializer.data, 'comments': comment_serializer.data})

class CookingList(BaseListView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(category='Cooking')
        serializer = ArticleSerializer(articles, many=True)
        return render(request, 'Cooking.html', {'articles': serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            new_article_id = serializer.data.get('id')
            return redirect('articles:Cooking_detail', pk=new_article_id)  # 여기에서 패턴 이름을 수정
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_new_post_page(cls, request):
        return render(request, 'newlist.html')

class CookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(category='Cooking')
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # 댓글을 가져오는 부분 추가
        comments = instance.comments.all()
        comment_serializer = CommentSerializer(comments, many=True)

        return render(request, 'Cooking_detail.html', {'article': serializer.data, 'comments': comment_serializer.data})



class CommentGetPost(APIView):
    def get(self, request, article_id):  # article_id로 수정
        article = get_object_or_404(Article, pk=article_id)  # pk 대신 article_id 사용
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_id):  # article_id로 수정
        article = get_object_or_404(Article, pk=article_id)  # pk 대신 article_id 사용
        serializer = CommentSerializer(data=request.data, context={'article': article, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CommentPutDelete(APIView):
    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)

    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        data = {"detail": "댓글이 삭제 되었습니다."}
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
