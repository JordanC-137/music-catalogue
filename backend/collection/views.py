from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404
from rest_framework import generics, status

from collection.models import Album, Rating
from collection.serializers import AlbumSerializer, RatingSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        #Get album and check for relevant rating
        album = self.get_object(pk)

    def delete(self, request, pk, format=None):
        album = self.get_object(pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    
    def get_queryset(self):
        return Rating.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)