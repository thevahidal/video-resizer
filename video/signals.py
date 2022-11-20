from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Video
from .tasks import resize_video


@receiver(post_save, sender=Video, dispatch_uid="resize_video")
def resize_video_handler(sender, instance, created, **kwargs):
    if created:
        resize_video.delay(instance.id)
        

@receiver(post_delete, sender=Video, dispatch_uid="delete_video_files")
def delete_video_files_handler(sender, instance, **kwargs):
    instance.file.delete(save=False)
    instance.file_240.delete(save=False)
    instance.file_360.delete(save=False)