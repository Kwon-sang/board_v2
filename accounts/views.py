from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class UserCreateView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup_form.html'
    success_url = reverse_lazy('board:index')
