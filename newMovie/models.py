from django.db import models

# Create your models here.


class newMovieModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    ratings = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
