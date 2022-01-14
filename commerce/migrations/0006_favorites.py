# Generated by Django 3.2.9 on 2022-01-14 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commerce', '0005_centeropinion_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='time')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Favorites', to='commerce.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Favorites', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]