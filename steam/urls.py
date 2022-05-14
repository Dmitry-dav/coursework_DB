from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='news'),
    path('games/', GamesPageView.as_view(), name='games'),
    path('developers/', DevelopersPageView.as_view(), name='developers'),
    path('publishers/', PublishersPageView.as_view(), name='publishers'),
]
