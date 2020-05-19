from django.contrib import admin

from .models import *


@admin.register(UserInfo)
class AdminGenre(admin.ModelAdmin):
    list_display = ('user', 'profession', 'created')
    # prepopulated_fields = {'slug': ('name',)}
