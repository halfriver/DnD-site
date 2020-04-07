from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from characters.models import Character

class CharacterList(ListView):
    model = Character
    context_object_name = "characters"

    def get_queryset(self, **kwargs):
        queryset = Character.objects.all()
        return queryset

    # **kwargs = can take any number of keyword arguments, without needing to specify them
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blub'] = "Quinn"
        return context


class CharacterDetail(DetailView):
    model = Character

    def get_queryset(self, **kwargs):
        queryset = Character.objects.filter(id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
