from django.contrib import admin

from jamil_bot.models import VehicleModel, UsernameModel


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']
    list_filter = ['name', 'color']


@admin.register(UsernameModel)
class UsernameModelAdmin(admin.ModelAdmin):
    list_display = ['tg_username', 'name', 'number']
    search_fields = ['tg_username', 'name', 'number']
    list_filter = ['tg_username', 'name', 'number']