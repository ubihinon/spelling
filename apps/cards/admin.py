from django.contrib import admin

from apps.cards.models import Card


@admin.register(Card)
class Card(admin.ModelAdmin):
    pass
