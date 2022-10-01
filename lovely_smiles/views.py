from django.shortcuts import render
from django.views.generic import TemplateView

class ServicesView(TemplateView):
    """
    View to render services page
    """
    template_name = 'lovely_smiles/services.html'


class HomeView(TemplateView):
    """
    View to render services page
    """
    template_name = 'lovely_smiles/index.html'
