from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from boardgames.models import BoardGameGenre, BoardGame, Event
from django.utils import timezone

BOARDGAME_LIST_URL = reverse("boardgames:board-game-list")
EVENT_LIST_URL = reverse("boardgames:event-list")


class PublicBoardGameTests(TestCase):
    def test_login_not_required_for_boardgames(self):
        res = self.client.get(BOARDGAME_LIST_URL)
        self.assertEqual(res.status_code, 200)

    def test_login_required_for_events(self):
        res = self.client.get(EVENT_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateBoardGameTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user", password="test123"
        )
        self.client.force_login(self.user)

    def test_boardgame_list_view(self):
        genre = BoardGameGenre.objects.create(name="Strategy")
        game1 = BoardGame.objects.create(
            title="Azul",
            genre=genre,
            min_players=2,
            max_players=4,
            description="Tiles",
            image_url="https://example.com"
        )
        game2 = BoardGame.objects.create(
            title="Catan",
            genre=genre,
            min_players=3,
            max_players=4,
            description="Trading",
            image_url="https://example.com"
        )
        res = self.client.get(BOARDGAME_LIST_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "boardgames/boardgame_list.html")
        self.assertIn(game1, res.context["boardgames"])
        self.assertIn(game2, res.context["boardgames"])


class PrivateEventTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user", password="test123"
        )
        self.client.force_login(self.user)

    def test_event_list_view(self):
        genre = BoardGameGenre.objects.create(name="Party")
        game = BoardGame.objects.create(
            title="Dixit",
            genre=genre,
            min_players=3,
            max_players=6,
            description="Imagination game",
            image_url="https://example.com"
        )
        event = Event.objects.create(
            title="Dixit Night",
            host=self.user,
            game=game,
            date=timezone.now() + timezone.timedelta(days=1),
            location="Cafe",
            description="Creative fun"
        )
        res = self.client.get(EVENT_LIST_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "boardgames/event_list.html")
        self.assertIn(event, res.context["events"])
