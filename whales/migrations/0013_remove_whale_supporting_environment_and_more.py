# Generated by Django 4.0.4 on 2022-04-23 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0003_remove_environment_threats'),
        ('threats', '0003_alter_threats_description'),
        ('whales', '0012_whale_supporting_environment_whale_threat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whale',
            name='supporting_environment',
        ),
        migrations.AlterField(
            model_name='whale',
            name='environment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whales', to='environment.environment'),
        ),
        migrations.AlterField(
            model_name='whale',
            name='threat',
            field=models.ManyToManyField(blank=True, related_name='whales', to='threats.threats'),
        ),
    ]
