from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["content", "created_at", "updated_at", "user"]

    def get_user(self, obj):
        return obj.user.username

    def create(self, validated_data):
        article_pk = self.context.get('view').kwargs.get('article_pk')
        article = Article.objects.get(id=article_pk)
        validated_data['article'] = article
        return super().create(validated_data)



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

