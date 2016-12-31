# Create your views here.
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render

from core.models import Event


class EventsView(TemplateView):
    model = Event
    template_name = 'events.html'

def landing(request):
    context = {}

    return render(request, 'index.html', context)