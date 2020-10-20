from django.db import models
from django.template.defaultfilters import truncatechars
# Create your models here.
from pets.models import Pet


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()

    def __str__(self):

        return f'{truncatechars(self.comment,5)}'
