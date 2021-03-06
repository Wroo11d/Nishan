# Generated by Django 3.2.9 on 2022-01-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_center_is_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='latitude',
            field=models.CharField(default=0, max_length=255, verbose_name='latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='center',
            name='longitude',
            field=models.CharField(default=0, max_length=255, verbose_name='longitude'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='center',
            name='location',
            field=models.CharField(default=0, max_length=255, verbose_name='location'),
            preserve_default=False,
        ),
    ]
