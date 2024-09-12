from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404
from rest_framework import generics, status

from collection.models import Album, Rating
from collection.serializers import AlbumSerializer, RatingSerializer

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
        return serializer.save(user = self.request.user)

#TODO On update, should only be able to number of stars
class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()