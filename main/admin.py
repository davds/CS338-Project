from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from django.db import models

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Username/Date", {'fields': ["username", "name", "last_updated","content"]}),
        ("Cards", {"fields": ["cards"]})
    ]

class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Card", {'fields': ["title", "type", "items", "content"]}),
    ]

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Item", {'fields': ["key", "value"]}),
    ]


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(CardItem,ItemAdmin)
