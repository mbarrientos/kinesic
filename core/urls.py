from django.conf.urls import url

from core.views import LandingView, TourView, WhoIsSheView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing'),
    url(r'^tour/?', TourView.as_view(), name='tour'),
    url(r'^whoisshe/?$', WhoIsSheView.as_view(), name='whoisshe'),
]
