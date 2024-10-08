from django.contrib import admin
from gamestore import models
# Register your models here.

@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher',)

@admin.register(models.Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('game', 'review_score', 'times_bought',)