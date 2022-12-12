from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import Post, Comment

#게시글 시리얼라이저에 댓글 시리얼라이저가 포함되어야 해서 댓글 시리얼라이저가 더 위에 선언됨.
class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "profile", "post", "text")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")

class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) #nested serializer
    comments = CommentSerializer(many=True, read_only=True) #댓글 시리얼라이저를 포함해서 댓글을 추가함.
    #many=True를 통해서 다수의 댓글 포함

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image", "published_date", "likes", "comments")

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")