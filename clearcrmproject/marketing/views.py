from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    template_name = 'makerting/home.html'

