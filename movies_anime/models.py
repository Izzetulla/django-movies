from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name