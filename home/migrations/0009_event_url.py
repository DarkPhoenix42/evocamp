# Generated by Django 4.2.6 on 2023-10-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_event_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, max_length=150),
        ),
    ]
