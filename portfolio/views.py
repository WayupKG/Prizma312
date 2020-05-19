from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from taggit.models import Tag

from .forms import *


class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio.html'


class CreatePortfolioView(FormView):
    template_name = 'portfolio/add_portfolio.html'
    form_class = PortfolioForm
    success_url = '/'

    def form_valid(self, form):
        pro = form.save(commit=False)
        pro.user = self.request.user
        pro.save()
        form.save_m2m()
        return super().form_valid(form)


