# Generated by Django 3.2.9 on 2021-12-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0078_auto_20211225_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='centeropinion',
            name='rate',
            field=models.DurationField(blank=True, null=True, verbose_name='rate'),
        ),
    ]
