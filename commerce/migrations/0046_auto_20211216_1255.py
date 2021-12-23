# Generated by Django 3.2.9 on 2021-12-16 09:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0045_auto_20211216_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_image',
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='service/', verbose_name='image')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='commerce.service')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]