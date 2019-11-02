from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.
class TitleView(TemplateView):
    template_name = 'title.html'

    def get(self, request, *args, **kwargs):
        context = super(TitleView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)