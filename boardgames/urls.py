from django.urls import path


from boardgames.views import index, BoardGameListView, EventListView, PlayerListView

urlpatterns = [
    path("", index),
    path("boardgames/", BoardGameListView.as_view(), name="board-game-list"),
    path("events/", EventListView.as_view(), name="event-list"),
    path("players/", PlayerListView.as_view(), name="player-list")
]
