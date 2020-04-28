#LIAM CORLEY \\ 2020

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views import generic

from .models import *

#View for index - main landing page
class IndexView(TemplateView):
    template_name = 'index.html'

    #pass context data to view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Queryset of all shows, sorted by sort_order (ascending)
        context['show_list'] = Show.objects.order_by('sort_order')
        #Queryset of all departments
        context['department_list'] = Department.objects.all()
        return context


#View for show detail page
#Template is show_detail.html, this is set in urls.py
class ShowDetailView(generic.DetailView):
    model = Show

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_list'] = Department.objects.all()
        return context
