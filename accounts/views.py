from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView,LogoutView)
from django.utils import timezone
from django.views import generic
from django.urls import reverse_lazy

from .forms import UserCreateForm,LoginForm

# Create your views here.
#新規ユーザアカウント登録
class CreateAccountView(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/create_account.html'
    success_url = reverse_lazy('/login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return redirect(self.get_success_url())

#ログイン機能
class AccountLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class AccountLogoutView(LoginRequiredMixin,LogoutView):
    tamplate_name = 'accounts/login.html'
