from os import name
from django.db import models
# Create your models here.


class Music(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    album = models.ForeignKey(
        'Album', on_delete=models.SET_NULL, null=True, blank=True)
    audio_file = models.FileField(upload_to='musics/')
    cover_image = models.ImageField(upload_to='music_image/')

    def __str__(self):
        return self.title

    class META:
        ordering = ["title"]


class Album(models.Model):
    name = models.CharField(max_length=400)
