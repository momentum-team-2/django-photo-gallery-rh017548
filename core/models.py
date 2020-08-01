from django.db import models
from users.models import User, AbstractUser
from django.conf import settings

# Create your models here.


#class User(AbstractUser):
#    pass


class Picture(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(
        null = True, blank = True,
        height_field='photo height',
        width_field='photo width',
        )
    uploaded_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='books')
    photo_height = models.PositiveIntegerField(null=True, blank=True)
    photo_weight = models.PositiveIntegerField(null=True, blank=True)