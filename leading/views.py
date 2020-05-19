from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


class IndexView(TemplateView):
    template_name = 'leading/index.html'