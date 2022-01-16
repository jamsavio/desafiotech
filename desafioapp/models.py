from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)

    def __str__(self):
        return self.name