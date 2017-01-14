from django.db import models
from django.db.models import fields
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):

    title = fields.CharField(max_length=100, verbose_name=_('Title and venue'))
    description = fields.TextField(blank=True, verbose_name=_('Long description'))
    date = fields.DateTimeField(verbose_name=_('Date of the event'))
    tickets_info = fields.URLField(blank=True, verbose_name=_('Link to buy tickets'))

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

class GalleryPhoto(models.Model):

    title = fields.CharField(max_length=100, blank=True, null=True, verbose_name=_('Gallery Photo'))
    image = models.ImageField(upload_to='gallery_photos/')
    uploaded_at = fields.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'gallery photo'
        verbose_name_plural = 'gallery photos'