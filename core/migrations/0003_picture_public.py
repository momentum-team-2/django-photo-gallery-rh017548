# Generated by Django 3.0.8 on 2020-08-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200801_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
