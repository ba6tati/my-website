from django.contrib import admin

from .models import App

class AppAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'version')

admin.site.register(App, AppAdmin)