# Generated by Django 4.2.6 on 2023-10-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.IntegerField(choices=[(1, 'Technical'), (2, 'Cultural'), (3, 'Bhawan-Related'), (4, 'Misc.')], default=4),
        ),
    ]
