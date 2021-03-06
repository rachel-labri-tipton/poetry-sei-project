# Generated by Django 4.0.4 on 2022-04-23 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0003_remove_environment_threats'),
        ('whales', '0009_alter_whale_environment_remove_whale_threat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whale',
            name='supporting_environment',
        ),
        migrations.AlterField(
            model_name='whale',
            name='environment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name', to='environment.environment'),
        ),
    ]
