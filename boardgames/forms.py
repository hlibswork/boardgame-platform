from django import forms


class BoardGameGenreSearchForm(forms.Form):
    genre = forms.CharField(max_length=255, required=False)


class EventGameSearchForm(forms.Form):
    game = forms.CharField(max_length=255, required=False)
