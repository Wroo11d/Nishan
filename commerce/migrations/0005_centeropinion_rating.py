# Generated by Django 3.2.9 on 2022-01-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_auto_20220103_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='centeropinion',
            name='rating',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, verbose_name='rating'),
            preserve_default=False,
        ),
    ]
