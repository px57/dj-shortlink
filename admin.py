from django.contrib import admin
from shortlink.models import ShortLink

@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('short_link', 'original_link', 'profile', 'created_on')
