from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()  # 사용자명 표시
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # 시간 표시

    class Meta:
        model = Comment
        fields = ['content', 'user', 'created_at']
    
    def get_user(self, obj):
        return obj.user.username if obj.user else None

    def create(self, validated_data):
        validated_data['article'] = self.context.get('article')  # article을 가져오는 방법 수정
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'likes_count', 'category', 'author']
        extra_kwargs = {
            'author': {'read_only': True}
        }

    def create(self, validated_data):
        if 'request' in self.context:
            validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


