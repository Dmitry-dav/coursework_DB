from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView

from .models import News, Game, Developer
from .utils import *


class MainPageView(ListView):
    template_name = 'steam/index.html'
    model = News
    context_object_name = 'news'
    extra_context = {'title': 'Новости'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = header
        return context


class GamesPageView(ListView):
    model = Game
    template_name = 'steam/games.html'
    context_object_name = 'game'
    extra_context = {'title': 'Игры'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = header
        return context


class DevelopersPageView(ListView):
    model = Developer
    template_name = 'steam/developers.html'
    context_object_name = 'developers'
    extra_context = {'title': 'Разработчики'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = header
        return context



def get_one_game(request, id: int):
    if request.method == "GET":
        template_name = 'steam/game.html'
        game = Game.objects.get(pk=id)
        context = {
                    "title": f"{game.title}",
                    "header": header,
                    "game": game,
                }
        return render(request, template_name, context)
