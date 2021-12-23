# Generated by Django 3.2.9 on 2021-12-16 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0050_auto_20211216_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='service',
        ),
        migrations.AddField(
            model_name='service',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='commerce.center'),
        ),
    ]