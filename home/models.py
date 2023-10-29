from django.db import models

# Create your models here.


class Event(models.Model):
    type_choices = [('Technical', 'Technical'), ('Cultural', 'Cultural'),
                    ('Bhawan-Related', 'Bhawan-Related'), ('Misc.', 'Misc.')]
    bhawan_choices = [('All', 'All'), ('Rajendra', 'Rajendra'),
                    ('Jawahar', 'Jawahar'), ('Rajiv', 'Rajiv'),('Govind','Govind'),('Ravindra','Ravindra'),('Radhakrishnan','Radhakrishnan'),('Kasturba','Kasturba'),('Sarojini','Sarojini')]
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField()
    venue = models.CharField(max_length=120, blank=False)
    start_time = models.DateTimeField(blank=False)
    image = models.ImageField(blank=True, upload_to='./media/event_imgs/')
    bhawan_specifier = models.CharField(max_length=100,choices=bhawan_choices,default='All')
    event_type = models.CharField(max_length=120, choices=type_choices)
    url = models.URLField(max_length=150, blank=True)