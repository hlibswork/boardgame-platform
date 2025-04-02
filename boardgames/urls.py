from django.urls import path
from boardgames.views import index, BoardGameListView, EventListView, PlayerListView, BoardGameDetailView, \
    EventDetailView, EventCreateView, toggle_assign_to_event

app_name = "boardgames"
urlpatterns = [
    path("", index, name="index"),
    path("boardgames/", BoardGameListView.as_view(), name="board-game-list"),
    path("events/", EventListView.as_view(), name="event-list"),
    path("players/", PlayerListView.as_view(), name="player-list"),
    path("boardgames/<int:pk>", BoardGameDetailView.as_view(), name="board-game-detail"),
    path("events/<int:pk>", EventDetailView.as_view(), name="event-detail"),
    path("events/create", EventCreateView.as_view(), name="event-create"),
    path("events/<int:pk>/toggle/", toggle_assign_to_event, name="event-toggle"),
]
