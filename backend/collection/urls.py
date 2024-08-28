from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('collections/', views.album_list, name="album_list"),
    path('collections/<int:pk>', views.album_detail, name="album_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)