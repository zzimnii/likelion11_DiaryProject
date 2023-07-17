from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'title', 'content' ]

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [ 'comment', 'post' ]