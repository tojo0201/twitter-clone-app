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