from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

from gamestore.models import Game

# Create your views here.
class GamesList(ListView):
    template_name = 'game_store/games_list.html'
    model = Game
    context_object_name = 'games'

class GamesDetail(DetailView):
    template_name = 'game_store/games_detail.html'
    model = Game
    context_object_name = 'game'

class GamesUpdate(UpdateView):
    template_name = 'game_store/game_form.html'
    model = Game
    fields = ['title', 'description', 'price', 'version']

    def get_success_url(self):
        return reverse_lazy('games_detail', kwargs={'pk': self.object.pk})

class GamesDelete(DeleteView):
    template_name = 'game_store/game_confirm_delete.html'
    model = Game
    success_url = reverse_lazy('game_list')

class GamesCreate(CreateView):
    template_name = 'game_store/game_create.html'
    model = Game
    fields = ['title', 'description', 'price', 'version']
    success_url = reverse_lazy('game_list')

