# Generated by Django 4.0.4 on 2022-04-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threats', '0002_threats_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threats',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]