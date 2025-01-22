from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crops/')

    def __str__(self):
        return self.name