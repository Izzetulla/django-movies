from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name