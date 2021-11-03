from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.db.models import Q
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from django.views import generic

from .models import Tweet
from .forms import TweetForm

# Create your views here.
#ツイートの一覧表示
def top(request):
#    follow_list = Follow.objects.filter(user=request.user).values_list('followed_user', flat=True)
#    tweet_list = Tweet.objects.filter(Q(user=request.user) | Q(user__in=follow_list))
    tweet_list = Tweet.objects.filter(user=request.user)
    tweet_list = tweet_list.order_by('created_time').reverse()[:20]
    return render(request, 'twitter/top.html', {'tweet_list': tweet_list})

#ツイートする画面
def tweet(request):
    form = TweetForm
    return render(request, 'twitter/tweet.html', {'form': form})


#ツイート処理
class TweetInputView(generic.CreateView):
    form_class = TweetForm
    template_name = 'twitter/tweet.html'
    success_url = reverse_lazy('twitter:top')

    def form_valid(self, form):
        tweet_contents = form.save(commit=False)
        user_contents = self.request.user
        tweet_contents.user = user_contents
        tweet_contents.save()
        self.object = user_contents
        return redirect(self.get_success_url())
