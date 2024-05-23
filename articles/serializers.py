from rest_framework import serializers
from .models import Travel, Camping, Leisure, Cooking, Comments

class BaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'content', 'created_at']

class TravelSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = Travel

class CampingSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = Camping

class LeisureSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = Leisure

class CookingSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = Cooking

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'content', ]
