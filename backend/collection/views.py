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

class RatingList(APIView):
    def get(self, request, format=None):
        ratings = Rating.objects.filter(user_id=request.user.id)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

#TODO figure out how to restrict user to only post their own value, maybe add extra value to RatingSerializer constructor
    def post(self, request, format=None):
        serializer = RatingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print("Saved")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
