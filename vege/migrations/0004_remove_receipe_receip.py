# Generated by Django 5.0.3 on 2024-06-07 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_receipe_receip_receipe_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='receip',
        ),
    ]
