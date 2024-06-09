from django.contrib import admin

from app.models import Applications, Blog


@admin.register(Applications)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'date']