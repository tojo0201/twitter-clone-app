from django.contrib import admin
from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.top, name='top'),
    path('tweet-input/', views.TweetInputView.as_view(), name='tweet_input'),
    path('user-list/', views.UserListView.as_view(), name='user_list'),
    path('tweet-user/<int:tweet_user_id>/', views.tweet_user, name='tweet_user'),
    path('follow/<int:tweet_user_id>/', views.user_follow, name='follow'),
    path('follow-deleted/<int:tweet_user_id>/', views.follow_deleted, name='follow_deleted'),
]
