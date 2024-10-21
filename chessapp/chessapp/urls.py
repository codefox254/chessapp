# chessapp/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chess.urls')),  # Include URLs from the chess app
]
