# Generated by Django 5.0.6 on 2024-05-29 16:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_mikrotik_ip_session_mikrotik_ip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='DNS_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='hotspot_server_name',
            field=models.CharField(default='null', max_length=64),
            preserve_default=False,
        ),
    ]
