import subprocess
from django.utils import timezone
from django.conf import settings
from celery import shared_task

from .models import Video


@shared_task()
def resize_video(video_id):
    video = Video.objects.get(id=video_id)
    print(f'Resizing video {video.file.url} started')
    video.resizing_started_at = timezone.now()
    
    subprocess.call([
        'ffmpeg',
        '-i',
        video.file.path,
        '-vf',
        'scale=240:-2',
        video.file.path.replace('.', '_240.'),
    ])

    subprocess.call([
        'ffmpeg',
        '-i',
        video.file.path,
        '-vf',
        'scale=360:-2',
        video.file.path.replace('.', '_360.'),
    ])

    video.resizing_finished_at = timezone.now()
    video.file_240 = video.file.url.replace('.', '_240.').replace(settings.MEDIA_URL, '')
    video.file_360 = video.file.url.replace('.', '_360.').replace(settings.MEDIA_URL, '')
    
    video.save()
    
    print(f'Resizing video {video.file.url} finished')
    
    return 