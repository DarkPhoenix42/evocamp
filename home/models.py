from django.db import models

# Create your models here.


class Event(models.Model):
    type_choices = [(1, 'Technical'), (2, 'Cultural'),
                    (3, 'Bhawan-Related'), (4, 'Misc.')]

    title = models.CharField(max_length=120, blank=False)
    description = models.TextField()
    venue = models.CharField(max_length=120, blank=False)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    image = models.ImageField(blank=True, upload_to='./media/event_imgs/')
    event_type = models.IntegerField(default=4, choices=type_choices)
