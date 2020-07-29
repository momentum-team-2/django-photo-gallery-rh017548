from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Picture(models.Model):
    title = models.CharField(max_length=255)
    imgage =
    added_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='books')
    