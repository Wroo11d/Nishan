# Generated by Django 3.2.9 on 2021-12-25 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0074_reservation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='service',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
    ]
