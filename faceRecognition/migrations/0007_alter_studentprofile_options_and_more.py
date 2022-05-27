# Generated by Django 4.0.4 on 2022-05-22 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faceRecognition', '0006_studentprofile_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentprofile',
            options={},
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
