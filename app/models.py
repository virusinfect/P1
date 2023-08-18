from django.db import models

class Founder(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='founder_images/')
    bio = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.name
