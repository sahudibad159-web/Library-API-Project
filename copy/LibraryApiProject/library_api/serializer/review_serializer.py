from rest_framework import serializers
from library_api.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Review
        fields = ["id", "username", "rating", "comment", "book"]
        read_only_fields = ["book", "user"]
