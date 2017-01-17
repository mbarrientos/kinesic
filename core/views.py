# Create your views here.
from django.views.generic import TemplateView, ListView
from django.views.generic.base import ContextMixin

from core.models import Event, GalleryPhoto

__all__ = ['TourView', 'LandingView', 'WhoIsSheView']


class TourView(ListView):
    model = Event
    template_name = 'events.html'


class LandingView(TemplateView, ContextMixin):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['gallery_photos'] = GalleryPhoto.objects.all()

        return context


class WhoIsSheView(TemplateView):
    template_name = 'whoisshe.html'
