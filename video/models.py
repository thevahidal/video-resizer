from django.db import models


class Video(models.Model):
    file = models.FileField(upload_to="videos")
    file_240 = models.FileField(upload_to="videos", blank=True)
    file_360 = models.FileField(upload_to="videos", blank=True)
    
    resizing_started_at = models.DateTimeField(blank=True, null=True)
    resizing_finished_at = models.DateTimeField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def resizing_duration(self):
        if self.resizing_started_at and self.resizing_finished_at:
            return self.resizing_finished_at - self.resizing_started_at
        return None
    
    @property
    def resizing_done(self):
        return bool(self.file_240 and self.file_360)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.file.name