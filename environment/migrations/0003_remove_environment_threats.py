# Generated by Django 4.0.4 on 2022-04-23 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0002_environment_threats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment',
            name='threats',
        ),
    ]
