from django.db import models
from django.db.models import fields
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):

    title = fields.CharField(max_length=100, verbose_name=_('Title and venue'))
    description = fields.TextField(null=True, verbose_name=_('Long description'))
    date = fields.DateTimeField(verbose_name=_('Date of the event'))
    tickets_info = fields.URLField(null=True, verbose_name=_('Link to buy tickets'))

