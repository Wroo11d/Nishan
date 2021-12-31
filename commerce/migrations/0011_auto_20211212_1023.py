# Generated by Django 3.2.9 on 2021-12-12 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0010_auto_20211212_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='location',
        ),
        migrations.AddField(
            model_name='center',
            name='close_days',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='close_days'),
        ),
        migrations.AddField(
            model_name='center',
            name='close_time',
            field=models.TimeField(blank=True, max_length=255, null=True, verbose_name='close_time'),
        ),
        migrations.AddField(
            model_name='center',
            name='open_days',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='open_days'),
        ),
        migrations.AddField(
            model_name='center',
            name='open_time',
            field=models.TimeField(blank=True, max_length=255, null=True, verbose_name='open_time'),
        ),
        migrations.AddField(
            model_name='notification',
            name='time',
            field=models.TimeField(blank=True, max_length=255, null=True, verbose_name='time'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='service',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='commerce.service'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='time',
            field=models.TimeField(blank=True, max_length=255, null=True, verbose_name='time'),
        ),
    ]