from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from boardgames.models import Player, BoardGame, BoardGameGenre, Event


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="adminpass"
        )
        self.client.force_login(self.admin_user)

        self.genre = BoardGameGenre.objects.create(name="Strategy")
        self.game = BoardGame.objects.create(
            title="Catan",
            genre=self.genre,
            min_players=3,
            max_players=4,
            description="Strategy game",
            image_url="https://example.com",
        )
        self.host = get_user_model().objects.create_user(
            username="hostuser", password="123", role="Host"
        )
        self.event = Event.objects.create(
            title="Catan Night",
            host=self.host,
            game=self.game,
            date=timezone.now() + timezone.timedelta(days=1),
            location="Cafe",
            description="Event desc",
        )

    def test_boardgame_genre_displayed_in_admin(self):
        url = reverse("admin:boardgames_boardgame_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.game.title)
        self.assertContains(res, self.genre.name)

    def test_player_role_displayed_in_admin(self):
        url = reverse("admin:boardgames_player_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.host.username)
        self.assertContains(res, self.host.role)

    def test_event_fields_displayed_in_admin(self):
        url = reverse("admin:boardgames_event_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.event.title)
        self.assertContains(res, self.event.game.title)
