from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views import generic

from .models import *

class IndexView(TemplateView):
    template_name = 'Portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_list'] = Show.objects.order_by('sort_order')
        context['department_list'] = Department.objects.all()
        return context



class ShowDetailView(generic.DetailView):
    model = Show

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_list'] = Department.objects.all()
        return context
