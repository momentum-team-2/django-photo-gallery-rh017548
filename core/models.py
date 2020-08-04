from django.db import models
from users.models import User
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

# Create your models here.



class Album(models.Model):
    title = models.CharField(max_length = 255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    featured_photo = models.ForeignKey('Picture', on_delete=models.CASCADE, related_name= '+',  null=True, blank=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
    

class Picture(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo_photos/', null=True, blank=True)
    photo_thumbnail = ImageSpecField(
        source="photo",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 60},
        )
    uploaded_date = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='photos')
    albums = models.ManyToManyField(Album, related_name='photos', blank=True)

    class Meta:
        ordering = ['uploaded_date']

    def __str__(self):
        return f'{self.title} by {self.owner.username}'


class Comment(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)