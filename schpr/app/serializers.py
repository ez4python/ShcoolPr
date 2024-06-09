from rest_framework.serializers import ModelSerializer

from app.models import Blog


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'descriptions', 'name', 'date']
