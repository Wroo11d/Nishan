# Generated by Django 3.2.9 on 2021-12-31 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='advertising',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='advertisings/', verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='center',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('open_days', models.DateField(blank=True, max_length=255, null=True, verbose_name='open_days')),
                ('close_days', models.DateField(blank=True, max_length=255, null=True, verbose_name='close_days')),
                ('open_time', models.TimeField(blank=True, null=True, verbose_name='open_time')),
                ('close_time', models.TimeField(blank=True, null=True, verbose_name='close_time')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='location')),
                ('image', models.ImageField(upload_to='centers/', verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'label',
                'verbose_name_plural': 'labels',
            },
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='service/', verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('sender', models.CharField(max_length=255, verbose_name='sender')),
                ('time', models.TimeField(blank=True, max_length=255, null=True, verbose_name='time')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='notifications/', verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('time', models.TimeField(auto_now_add=True, max_length=255, verbose_name='time')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('latitude', models.CharField(max_length=255, verbose_name='latitude')),
                ('longitude', models.CharField(max_length=255, verbose_name='longitude')),
                ('location', models.CharField(max_length=255, verbose_name='location')),
                ('is_feature', models.BooleanField(verbose_name='is feature')),
                ('background_image', models.ImageField(upload_to='service/', verbose_name='background_image')),
                ('center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='commerce.center')),
                ('label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='commerce.label')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceOpinion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('rating', models.DecimalField(decimal_places=0, max_digits=1, verbose_name='rating')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='time')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ServiceOpinions', to='commerce.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ServiceOpinions', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service_image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='service/', verbose_name='image')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Service_images', to='commerce.service', verbose_name='service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='time')),
                ('is_active', models.BooleanField(verbose_name='is active')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='commerce.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CenterOpinion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='time')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CenterOpinions', to='commerce.center')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CenterOpinions', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Center_image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='center/', verbose_name='image')),
                ('center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Center_images', to='commerce.center', verbose_name='center')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
