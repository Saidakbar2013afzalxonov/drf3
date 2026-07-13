from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','created_at','title','body','updated_at','user']
        read_only_fields = ['id','created_at','updated_at']