import subprocess
from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from redis import Redis, exceptions
from decouple import config

from .models import Video


class FFMPEGTest(TestCase):
    def test_ffmpeg(self):

        try:
            subprocess.call(["ffmpeg", "-version"])
        except FileNotFoundError:
            self.fail("FFmpeg is not available")


class RedisTest(TestCase):
    def test_redis(self):
        redis_url = config("CELERY_BROKER_URL")
        r = Redis.from_url(redis_url)

        try:
            r.ping()
        except exceptions.ConnectionError:
            self.fail("Redis is not running")


class VideoResizingTest(TestCase):
    
    # remove test files after test
    def tearDown(self):
        video = Video.objects.get(id=self.video.id)
        video.file.delete()
        video.file_240.delete()
        video.file_360.delete()
        video.delete()
        
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def test_video_resizing(self):
        try:
            file = SimpleUploadedFile(
                "tests/sample_video.mp4", content=open("tests/sample_video.mp4", "rb").read(),  content_type="video/mp4"
            )
            self.video = Video.objects.create(
                file=file
            )
            
            self.video.refresh_from_db()
            
            assert self.video.file_240 == "videos/sample_video_240.mp4"
            assert self.video.file_360 == "videos/sample_video_360.mp4"
            
            assert self.video.resizing_done == True
            
        except Exception as e:
            self.fail(e)
