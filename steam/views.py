from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView

from .models import News, Game, Developer, Publisher
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
    template_name = 'steam/game.html'
    context_object_name = 'games'
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


class PublishersPageView(ListView):
    model = Publisher
    template_name = 'steam/publishers.html'
    context_object_name = 'publishers'
    extra_context = {'title': 'Издатели'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = header
        return context
