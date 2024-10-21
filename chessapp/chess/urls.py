# /chessapp/chess/urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, puzzles, play_bots, study, games

urlpatterns = [
    path('', index, name='home'),  # Main page
    path('puzzles/', puzzles, name='puzzles'),  # Puzzles page
    path('play_bots/', play_bots, name='play_bots'),  # Play bots page
    path('study/', study, name='study'),  # Study page
    path('games/', games, name='games'),  # Games page
]

# Only include this in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
