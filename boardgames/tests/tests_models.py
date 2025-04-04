from django.test import TestCase
from django.utils import timezone

from boardgames.models import (
    BoardGameGenre,
    BoardGame,
    Player,
    Event,
    Registration
)


class BoardGameModelsTest(TestCase):
    def setUp(self):
        self.genre = BoardGameGenre.objects.create(name="Strategy")
        self.boardgame = BoardGame.objects.create(
            title="Catan",
            genre=self.genre,
            min_players=3,
            max_players=4,
            description="A strategy game of trading and building.",
            image_url="https://example.com/catan.jpg"
        )
        self.player = Player.objects.create_user(
            username="testuser",
            password="testpass123",
            role="Player"
        )
        self.host = Player.objects.create_user(
            username="hostuser",
            password="hostpass123",
            role="Host"
        )
        self.event = Event.objects.create(
            title="Catan Evening",
            host=self.host,
            game=self.boardgame,
            date=timezone.now() + timezone.timedelta(days=1),
            location="Game Cafe",
            description="Evening of strategic fun"
        )

    def test_boardgamegenre_str(self):
        self.assertEqual(str(self.genre), "Strategy")

    def test_boardgame_str(self):
        self.assertEqual(str(self.boardgame), "Catan")

    def test_player_str(self):
        self.assertEqual(str(self.player), "Player testuser with Player role.")
        self.assertEqual(str(self.host), "Player hostuser with Host role.")

    def test_event_str(self):
        self.assertIn("Catan Evening", str(self.event))
        self.assertIn("Game Cafe", self.event.location)

    def test_registration_default_status(self):
        registration = Registration.objects.create(
            player=self.player,
            event=self.event
        )
        self.assertEqual(registration.status, "Registered")
        self.assertEqual(
            str(registration),
            f"Player {self.player.username} was Registered on {self.event}."
        )

    def test_player_favorite_games_many_to_many(self):
        self.player.favorite_games.add(self.boardgame)
        self.assertIn(self.boardgame, self.player.favorite_games.all())
