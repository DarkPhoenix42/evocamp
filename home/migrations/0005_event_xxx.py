# Generated by Django 4.2.6 on 2023-10-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='xxx',
            field=models.IntegerField(default=12),
        ),
    ]