from django.contrib import admin

# Register your models here.
from boardgames.models import BoardGame, Player, Event, Registration


@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ("title", "genre")
    list_filter = ("genre",)
    search_fields = ("title", "genre")


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("username", "role")
    list_filter = ("role",)
    search_fields = ("username", "role")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "host", "game", "date")
    list_filter = ("game", "date")
    search_fields = ("title", "host", "game", "date")


@admin.register(Registration)
class RegistrationGameAdmin(admin.ModelAdmin):
    list_display = ("player", "event", "status")
    list_filter = ("event", "status")
    search_fields = ("player", "event", "status")
