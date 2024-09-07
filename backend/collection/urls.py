from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('collection/', views.AlbumList.as_view(), name="album_list"),
    path('collection/<int:pk>', views.AlbumDetail.as_view(), name="album_detail"),
    path('collection/ratings', views.RatingList.as_view(), name="rating_list"),

]

urlpatterns = format_suffix_patterns(urlpatterns)