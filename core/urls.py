from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
]