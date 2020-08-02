from django.db import models
from users.models import User
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

# Create your models here.




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
    