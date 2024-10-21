from django.shortcuts import render

def index(request):
    """Render the home page."""
    context = {'title': 'Home Page'}  # Example context data
    return render(request, 'chess/index.html', context)

def puzzles(request):
    """Render the puzzles page."""
    return render(request, 'chess/puzzles.html')

def play_bots(request):
    """Render the play bots page."""
    return render(request, 'chess/play_bots.html')

def study(request):
    """Render the study page."""
    return render(request, 'chess/study.html')

def games(request):
    """Render the games page."""
    return render(request, 'chess/games.html')
