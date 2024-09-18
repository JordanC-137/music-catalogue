from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404
from rest_framework import generics, status

from collection.models import Album, Rating
from collection.serializers import AlbumSerializer, RatingSerializer
from rest_framework.exceptions import ValidationError

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.all()

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    
    def get_queryset(self):
        return Rating.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        #Check if exists prior rating for this user
        initial_data = serializer.get_initial()
        album = initial_data['album']
        prior_rating = Rating.objects.filter(user=self.request.user).filter(album=album)
        if prior_rating:
            raise ValidationError("Already exists prior version")
        else:
            return serializer.save(user = self.request.user)

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()