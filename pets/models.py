from django.db import models


# Create your models here.
class Pet(models.Model):
    PET_TYPE = (
        ('c', 'cat'),
        ('d', 'dog'),
        ('p', 'parrot'),
    )
    type = models.CharField(max_length=6, choices=PET_TYPE)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField()


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
