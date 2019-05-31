from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import url, include

urlpatterns = [
    url('', include('dataScience.urls')),
]
