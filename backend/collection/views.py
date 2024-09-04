from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404
from rest_framework import generics

from collection.models import Album
from collection.serializers import AlbumSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404