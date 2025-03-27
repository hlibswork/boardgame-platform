from django.urls import path

from boardgames.views import index

urlpatterns = [
   path("", index)
]
