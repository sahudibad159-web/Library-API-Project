from rest_framework import serializers
from library_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
