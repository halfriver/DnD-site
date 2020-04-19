from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

    # def get_queryset(self, **kwargs):
    #     queryset = Character.objects.filter(id=self.kwargs['pk'])
    #     return queryset
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
