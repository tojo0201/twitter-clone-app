from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView,LogoutView)
from django.utils import timezone
from django.views import generic

from .forms import UserCreateForm,LoginForm

# Create your views here.
#新規ユーザアカウント登録
class CreateAccountView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            return redirect('/login')
        return render(request, 'accounts/create_account.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'accounts/create_account.html', {'form': form,})

#ログイン機能
class AccountLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class AccountLogoutView(LoginRequiredMixin,LogoutView):
    tamplate_name = 'accounts/login.html'
