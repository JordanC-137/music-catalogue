from rest_framework import serializers
from collection.models import Artist, Album, Rating
from django.contrib.auth.models import User

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class RatingSerializer(serializers.Serializer):
    stars = serializers.IntegerField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)
