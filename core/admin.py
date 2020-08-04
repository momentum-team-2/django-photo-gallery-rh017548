from django.contrib import admin
from .models import Picture, Album, Comment

# Register your models here.
admin.site.register(Picture)
admin.site.register(Album)
admin.site.register(Comment)