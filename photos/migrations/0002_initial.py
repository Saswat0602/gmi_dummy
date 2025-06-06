# Generated by Django 5.2.1 on 2025-06-04 09:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0001_initial'),
        ('projects', '0002_initial'),
        ('sheets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='sheets',
            field=models.ManyToManyField(blank=True, related_name='photos', to='sheets.sheet'),
        ),
        migrations.AddField(
            model_name='photo',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photoannotation',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photoannotations', to='photos.photo'),
        ),
        migrations.AddField(
            model_name='photoannotation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photoannotations', to='projects.project'),
        ),
        migrations.AddField(
            model_name='photoannotation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
