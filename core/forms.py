from django import forms
from django.forms import ModelForm
from .models import Picture

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = [
            'title',
            'photo',
            'public',
            'owner',
        ]