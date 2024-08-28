from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

from collection.models import Album
from collection.serializers import AlbumSerializer

@csrf_exempt
def album_list(request):
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many = True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
def album_detail(request, pk):
    try:
        album = Album.objects.get(pk=pk)
    except album.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AlbumSerializer(album, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        album.delete()
        return HttpResponse(status=204)