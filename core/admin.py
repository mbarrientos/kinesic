from django.contrib import admin

from core.models import Event, GalleryPhoto


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at',)