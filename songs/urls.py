from django.urls import path

from .views import SongView

urlpatterns = [
    path("songs/", SongView.as_view()),
    path("songs/<int:pk>/songs/", SongView.as_view()),
]
