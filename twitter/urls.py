from django.contrib import admin
from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.top, name='top'),
    path('tweet-input/', views.TweetInputView.as_view(), name='tweet_input'),
]
