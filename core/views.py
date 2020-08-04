from .models import Picture, Album, Comment
from .forms import PictureForm, AlbumForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from users.models import User
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.

def home(request):
    photos = Picture.objects.all()
    form = PictureForm()
    if request.user.is_authenticated:
        return redirect('list_photo')
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


def edit_photo(request, pk):
    photo = get_object_or_404(request.user.photos, pk=pk)
    if request.method == 'POST':
        form = PictureForm(data=request.POST, instance=photo, files=request.FILES)
        if form.is_valid():
            photo = form.save()
            return redirect(to='list_photo')


def delete_photo(request, pk):
    photo = get_object_or_404(request.user.photos, pk=pk)
    if request.method == 'POST':
        photo.delete()
        messages.success(request, 'Picture deleted.')
        return redirect(to='list_photo')
    
    return render(request, 'core/delete_photo.html', {'photo': photo})
    

def list_photo(request):
    photos = Picture.objects.all()
    # answers = request.user.response.all()
    
    return render(request, 'core/list_photo.html', {'photos': photos})


def show_photo(request, pk):
    photo = get_object_or_404(Picture.objects.all(), pk=pk)
    comments = photo.comments.order_by('created_on')
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, files=request.FILES )
        if comment_form.is_valid():
             new_comment = comment_form.save(commit=False)
             new_comment.picture = photo
             new_comment.save()
             return redirect(to='show_photo', pk=pk)
    else:
        comment_form = CommentForm()
    
        
    return render(request, 'core/show_photo.html', {'photo': photo, 'pk': pk, 'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return redirect(to='list_album')
    else:
        form = AlbumForm()
    return render(request, 'core/add_album.html', {'form': form})


def list_album(request):
    albums = request.user.albums.all()
    form = AlbumForm()
    return render(request, 'core/list_album.html', {'albums': albums, 'form':form})


def show_album(request, pk):
    album = get_object_or_404(request.user.albums, pk=pk)
    form = AlbumForm()
    photos = album.photos.all().order_by('uploaded_at')
    return render(request, 'core/show_album.html', {'album': album, 'pk': pk, 'form': form, 'photos': photos,})


def edit_album(request, pk):
    album = get_object_or_404(request.user.albums, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect(to='list_album')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'core/edit_album.html', {'form': form, 'album': album})


def delete_album(request, pk):
    album = get_object_or_404(request.user.albums, pk=pk)
    if request.method == 'POST':
        album.delete()
        messages.success(request, 'Album deleted.')
        return redirect(to='list_album')

    return render(request, 'core/delete_album.html', {'album': album })
