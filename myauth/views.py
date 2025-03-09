from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from myauth.models import CustomUser
from myauth.forms import SignupForm


class CustomLoginView(LoginView):
    template_name = 'myauth/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True


class CustomSignUpView(CreateView):
    form_class = SignupForm
    template_name = 'myauth/signup.html'
    success_url = '/home'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_player = True
        user.save()
        return super().form_valid(form)
