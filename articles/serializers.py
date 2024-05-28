from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",)


class ArticleSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'likes_count','category','author']
        extra_kwargs = {
            'author':{'read_only': True}
        }

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

