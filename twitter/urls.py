from django.contrib import admin
from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.top, name='top'),
    path('tweet-input/', views.TweetInputView.as_view(), name='tweet_input'),
    path('user-list/', views.UserListView.as_view(), name='user_list'),
    path('other-user/<int:other_user_id>/', views.other_user, name='other_user'),
    path('followed/<int:other_user_id>/', views.user_followed, name='followed'),
    path('follow-deleted/<int:other_user_id>/', views.follow_deleted, name='follow_deleted'),
]
