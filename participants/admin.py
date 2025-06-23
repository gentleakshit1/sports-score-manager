from django.apps import AppConfig
from django.contrib import admin
from .models import Department, Team, Player

class ParticipantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'participants'
    verbose_name = 'Participants Management'  # Optional, nice display in Django Admin

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    list_filter = ('department',)
    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team', 'role', 'jersey_number')
    list_filter = ('team', 'role')
    search_fields = ('name', 'email', 'whatsapp_number')