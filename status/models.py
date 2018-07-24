from django.conf import settings
from django.db import models




def upload_status_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


# Create your models here.
class Status(models.Model): #fb status, instagram post, tween, linkedin post
    user            = models.ForeignKey(settings.AUTH_USER_MODEL) # user instance .save
    content         = models.TextField(null=True, blank=True)
    image           = models.ImageField(upload_to=upload_status_image, null=True, blank=True) # great 3rd part package = django storanges --> AWS#pip install pillow to handle images
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = StatusManager

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = "Status post"
        verbose_name_plural = "Status posts"



