from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django_filters.views import FilterView
from rest_framework import viewsets

from gamestore.models import Game, Publisher, Developer, Genre, Statistics
from gamestore import filters
from gamestore import serializers

# Create your views here.
class PublisherAPI(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = serializers.Publisher

class GameAPI(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = serializers.Game

class DeveloperAPI(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = serializers.Developer

class GenreAPI(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.Genre

class StatisticsAPI(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = serializers.Statistics

class GamesList(FilterView):
    template_name = 'game_store/games_list.html'
    model = Game
    context_object_name = 'games'
    filterset_class = filters.Game

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

