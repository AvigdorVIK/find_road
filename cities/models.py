from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length= 500, null=True)


    def __str__(self):
        return self.name


