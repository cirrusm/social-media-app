from rest_framework import serializers

from .models import Tweet
MAX_TWEET_LENGTH = 240

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("Tweet must be less than 240 characters")
        return value