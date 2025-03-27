from django.shortcuts import render

from boardgames.models import BoardGame, Player, Event


def index(request):
    num_games = BoardGame.objects.count()
    num_players = Player.objects.count()
    num_events = Event.objects.count()

    context = {
        "num_games": num_games,
        "num_players": num_players,
        "num_events": num_events,
    }
    return render(request, "index.html", context=context)
