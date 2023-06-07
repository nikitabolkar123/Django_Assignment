from rest_framework import serializers
from .models import Like, Post


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'content', 'visibility', 'like_count']
        # read_only_fields = ['like']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']
