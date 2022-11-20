from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ["file_240", "file_360", "resizing_duration", "resizing_started_at", "resizing_finished_at", "created_at", "updated_at", ]
    list_display = ["id", "file", "created_at", "updated_at", "resizing_done", "resizing_duration"]