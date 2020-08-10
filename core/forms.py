from django import forms
from django.forms import ModelForm
from .models import Picture, Album, Comment

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = [
            'title',
            'photo',
            'public',
            
        ]


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'featured_photo',
            'public',
            
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'body', 
            
        ]