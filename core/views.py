# Create your views here.
from django.views.generic import TemplateView, ListView

from core.models import Event


class TourView(ListView):
    model = Event
    template_name = 'events.html'


class LandingView(TemplateView):
    template_name = 'index.html'
