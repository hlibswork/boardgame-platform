from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from boardgames.models import BoardGame, Player, Event


def index(request):
    num_games = BoardGame.objects.count()
    num_players = Player.objects.count()
    num_events = Event.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_games": num_games,
        "num_players": num_players,
        "num_events": num_events,
        "num_visits": num_visits + 1,
    }
    return render(request, "index.html", context=context)


class BoardGameListView(generic.ListView):
    model = BoardGame
    context_object_name = "boardgames"
    paginate_by = 5


class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    context_object_name = "events"
    paginate_by = 5

    def get_queryset(self):
        return Event.objects.filter(date__gte=timezone.now()).order_by("date")


class PlayerListView(LoginRequiredMixin, generic.ListView):
    model = Player
    context_object_name = "players"
    paginate_by = 5


class BoardGameDetailView(generic.DetailView):
    model = BoardGame
    context_object_name = "boardgame"


class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event
    context_object_name = "event"
