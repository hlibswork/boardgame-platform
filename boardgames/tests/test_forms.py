from django.test import TestCase

from boardgames.forms import BoardGameGenreSearchForm, EventGameSearchForm


class BoardGameGenreSearchFormTest(TestCase):
    def test_genre_search_form_valid(self):
        form_data = {"genre": "Strategy"}
        form = BoardGameGenreSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["genre"], "Strategy")

    def test_genre_search_form_empty_valid(self):
        form = BoardGameGenreSearchForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["genre"], "")


class EventGameSearchFormTest(TestCase):
    def test_game_search_form_valid(self):
        form_data = {"game": "Dixit"}
        form = EventGameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["game"], "Dixit")

    def test_game_search_form_empty_valid(self):
        form = EventGameSearchForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["game"], "")
