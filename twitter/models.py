import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
#ツイート
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=200)
    created_time = models.DateTimeField(default=timezone.now)
    deleted_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.tweet_text

class Follow(models.Model):
    #ユーザ情報
    follower = models.ForeignKey(User, related_name="follower_user", on_delete=models.CASCADE)
    followee = models.ForeignKey(User, related_name="followee_user", on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)

class FavoriteTweet(models.Model):
    #お気に入りにしているユーザ情報
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    #お気に入りのツイート情報
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)
