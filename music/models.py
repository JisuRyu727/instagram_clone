from django.db import models
from uuid import uuid4
from datetime import datetime

# Create your models here.

# 파일 경로 정의 메소드
def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/', ymd_path, uuid_name])

# 앨범 정보
class Album(models.Model):
    title = models.CharField(max_length=500)
    singer = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    release_date = models.DateTimeField(auto_now=False)
    last_update_datetime = models.DateTimeField(auto_now=True)
    last_update_pageId = models.CharField(max_length=100)

# 음악 객체 정보
class Music(models.Model):
    title = models.CharField(max_length=500)
    singer = models.CharField(max_length=200)
    playTime = models.IntegerField()
    country = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now=False)
    last_update_datetime = models.DateTimeField(auto_now=True)
    last_update_pageId = models.CharField(max_length=100)

class Uploaded_Music(models.Model):
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    last_update_datetime = models.DateTimeField(auto_now=True)
    last_update_pageId = models.CharField(max_length=100)
