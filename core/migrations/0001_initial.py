# Generated by Django 3.0.8 on 2020-08-01 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, height_field='photo height', null=True, upload_to='', width_field='photo width')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('photo_height', models.PositiveIntegerField(blank=True, null=True)),
                ('photo_weight', models.PositiveIntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
