from django.db import models

from django.contrib.auth.models import AbstractUser


class BoardGame(models.Model):
    title = models.CharField(max_length=255, unique=True)
    genre = models.CharField(max_length=255)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f"{self.title}"


class Player(AbstractUser):
    class Meta:
        ordering = ("username",)

    HOST_PLAYER_CHOICES = (
        ('Player', 'Player'),
        ('Host', 'Host'),
    )
    role = models.CharField(max_length=6, choices=HOST_PLAYER_CHOICES, default="Player")
    favorite_games = models.ManyToManyField(BoardGame, related_name="favorited_by")

    def __str__(self):
        return f"Player {self.username} with {self.role} role."


class Event(models.Model):
    class Meta:
        ordering = ["date"]
        unique_together = ("title", "date")

    title = models.CharField(max_length=255)
    host = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="hosted_events")
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="events")
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d %H:%M')}"


class Registration(models.Model):
    class Meta:
        unique_together = ("player", "event")

    REGISTER_CHOICES = (
        ('Registered', 'Registered'),
        ('Canceled', 'Canceled'),
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    status = models.CharField(max_length=10, choices=REGISTER_CHOICES, default="Registered")
    registered_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Player {self.player.username} was {self.status} on {self.event}."
