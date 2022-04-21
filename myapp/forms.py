from asyncio.windows_events import NULL
import imp
from pickle import TRUE
from turtle import title
from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=250)
    body = forms.CharField(widget=forms.Textarea)
    photo_url = forms.CharField(max_length=2500)
    