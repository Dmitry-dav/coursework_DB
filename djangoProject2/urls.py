from django.contrib import admin
from django.urls import path, include

from coursework import settings
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('steam.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
