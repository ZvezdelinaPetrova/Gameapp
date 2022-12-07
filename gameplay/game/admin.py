from django.contrib import admin

from gameplay.game.models import Game, Profile


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
