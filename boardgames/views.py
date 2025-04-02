from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from boardgames.models import BoardGame, Player, Event, Registration


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


class BoardGameDetailView(generic.DetailView):
    model = BoardGame
    context_object_name = "boardgame"


class BoardGameCreateView(LoginRequiredMixin, generic.CreateView):
    model = BoardGame
    fields = "__all__"
    success_url = reverse_lazy("boardgames:board-game-list")


class BoardGameDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = BoardGame
    fields = "__all__"
    success_url = reverse_lazy("boardgames:board-game-list")


class BoardGameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = BoardGame
    fields = "__all__"
    success_url = reverse_lazy("boardgames:board-game-list")


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




class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()

        registration = Registration.objects.filter(
            player=self.request.user, event=event
        ).first()

        context["registration"] = registration
        return context


class EventCreateView(LoginRequiredMixin, generic.CreateView):
    model = Event
    fields = "__all__"
    success_url = reverse_lazy("boardgames:event-list")


class EventDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Event
    fields = "__all__"
    success_url = reverse_lazy("boardgames:event-list")


class EventUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Event
    fields = "__all__"
    success_url = reverse_lazy("boardgames:event-list")


def toggle_assign_to_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    registration = Registration.objects.filter(
        player=request.user, event=event
    ).first()

    if registration:
        if registration.status == "Registered":
            registration.status = "Canceled"
        else:
            registration.status = "Registered"
        registration.save()
    else:
        Registration.objects.create(
            player=request.user, event=event, status="Registered"
        )

    return redirect("boardgames:event-detail", pk=pk)
