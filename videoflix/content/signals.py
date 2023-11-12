

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from content.models import Movie
from content.tasks import convert_videoformat
import django_rq
from django_rq import job

@receiver(post_save, sender=Movie)
@job # automatically use defaulte queue of django RQ
def movie_post_save(sender, instance, created, **kwargs): # function call after new movie instance created
    convert_videoformat(instance.file.path, '480')
    convert_videoformat(instance.file.path, '720')
    convert_videoformat(instance.file.path, '1080')
    if created:
        print('New video was just created')
    else:
        print('existing video was saved')


@receiver(post_delete, sender=Movie)
@job
def video_post_delete(sender, instance, **kwargs):
    print('video was deleted')

