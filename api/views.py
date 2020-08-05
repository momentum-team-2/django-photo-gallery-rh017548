from django.shortcuts import render
from rest_framework import views, viewsets
from core.models import Album, Picture
from api.serializers import AlbumSerializer, UserSerializer, PictureSerializer
from rest_framework import generics
from users.models import User
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers 
from rest_framework.generics import ListCreateAPIView


# Create your views here.

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'albums': reverse('album-list', request=request, format=format),
        'photos': reverse('photo-list', request=request, format=format),
    })

