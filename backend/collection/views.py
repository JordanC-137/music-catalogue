from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

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