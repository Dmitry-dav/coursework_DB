from django.contrib import admin

from .models import *

admin.site.register(News)
admin.site.register(Review)
admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Developer)

