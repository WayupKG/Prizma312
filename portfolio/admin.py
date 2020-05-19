from django.contrib import admin

from .models import *


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'created')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Portfolio)
class AdminPortfolio(admin.ModelAdmin):
    list_display = ('user', 'title', 'created')
    prepopulated_fields = {'slug': ('title',)}
