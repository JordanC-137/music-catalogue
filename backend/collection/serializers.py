from rest_framework import serializers
from collection.models import Artist, Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

#TODO currently trying to understand how to serialize foriegn key object for creating new Rating with user pre-selected
class RatingSerializer(serializers.Serializer):
    stars = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    album_id = serializers.IntegerField(read_only=True)
