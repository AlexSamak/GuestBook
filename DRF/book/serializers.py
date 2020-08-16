from rest_framework.serializers import ModelSerializer
from book.models import BookBase


class BookSerializer(ModelSerializer):
    class Meta:
        model = BookBase
        fields = ['name', 'comment', 'timestamp']
