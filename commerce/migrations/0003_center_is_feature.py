# Generated by Django 3.2.9 on 2022-01-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0002_advertising_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='is_feature',
            field=models.BooleanField(default=0, verbose_name='is feature'),
            preserve_default=False,
        ),
    ]