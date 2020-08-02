from .models import Picture
from .forms import PictureForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from users.models import User


# Create your views here.

def home(request):
    photos = Picture.objects.all()
    form = PictureForm()
    return render(request, 'core/home.html', {'photos': photos, 'form': form})


def add_photo(request):
    if request.method == 'POST':
        form = PictureForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            photo.save()
            return redirect(to='home')
    else:
        form = PictureForm()
    return render(request, 'core/add_photo.html', {'form': form})
