from django.template.context_processors import static
from django.urls import path
from django.conf.urls.static import static

from djangoProject2 import settings
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='news'),
    path('games/', GamesPageView.as_view(), name='games'),
    path('developers/', DevelopersPageView.as_view(), name='developers'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)