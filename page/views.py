from django.shortcuts import render
from django.views.generic import TemplateView

class UserForm(TemplateView):
    template_name = 'home.html'
    