from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Show, Image

class IndexView(generic.ListView):
    template_name = 'Portfolio/index.html'
    context_object_name = 'show_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Show.objects.order_by('sort_order')[:30]

class DetailView(generic.DetailView):
    model = Show
    template_name = 'Portfolio/detail.html'