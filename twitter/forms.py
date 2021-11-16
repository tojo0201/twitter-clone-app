from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from .models import Tweet

class TweetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    class Meta:
        model = Tweet
        fields = ('tweet_text',)
        labels = {
            'tweet_text': "",
        }
        widgets = {
            'tweet_text': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
