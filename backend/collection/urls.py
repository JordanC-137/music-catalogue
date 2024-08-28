from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.album_list, name="album_list"),
#    path('collections/<int:pk>', views.album_detail, name="album_detail"),
]
