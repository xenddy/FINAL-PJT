from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

    def create(self, validated_data):
        validated_data['article'] = self.context['article']
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


