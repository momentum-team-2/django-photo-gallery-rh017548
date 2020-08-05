from rest_framework import serializers
from core.models import Picture, Album
from users.models import User


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Picture
        fields = ['url', 'id', 'owner', 'photo']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    photos = PictureSerializer(many=True, read_only=True)

    
    class Meta:
        model = Album
        fields = ['url', 'id', 'title', 'featured_photo', 'owner', 'photos']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    albums = serializers.HyperlinkedRelatedField(many=True, view_name='album-detail', read_only = True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'albums']