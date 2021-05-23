from django.db import models

# Create your models here.
class works(models.Model):
    Name = models.CharField(max_length=30)
    Done  = models.BooleanField()
    Date = models.DateField()
    def __str__(self):
        return self.Name
    # python manage.py makemigrations
    # python manage.py migrate