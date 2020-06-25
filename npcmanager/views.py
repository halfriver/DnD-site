from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from characters.models import Character

class HomePageView(ListView):
    template_name = "npcmanager/npc.html"
    model = Character
    context_object_name = "characters"

    def get_queryset(self, **kwargs):
        queryset = Character.objects.all()
        return queryset
