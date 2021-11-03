from django.contrib import admin
from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('top/', views.top, name='top'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet_input/', views.TweetInputView.as_view(), name='tweet_input'),
]
