# Generated by Django 4.2.20 on 2025-03-26 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("boardgames", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={"ordering": ["date"]},
        ),
        migrations.AlterField(
            model_name="event",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="boardgames.boardgame",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="host",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="hosted_events",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="registration",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="registrations",
                to="boardgames.event",
            ),
        ),
        migrations.AlterField(
            model_name="registration",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="registrations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="event",
            unique_together={("title", "date")},
        ),
        migrations.AlterUniqueTogether(
            name="registration",
            unique_together={("player", "event")},
        ),
    ]
