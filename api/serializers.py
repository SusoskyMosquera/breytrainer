from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True, required=False)
    video = serializers.FileField(use_url=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'post_type', 'title', 'image', 'description', 'content', 'video', 'author_name', 'created_at']
