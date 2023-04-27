from django.contrib import admin

from .models import *


class ShopeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price', 'content')
    list_filter = ('is_published', 'time_create')

admin.site.register(Shopee, ShopeeAdmin)