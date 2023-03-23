from django.db import models


class Game(models.Model):
    title = models.TextField(unique=True)
    author = models.TextField(default='unknown')
    rating = models.IntegerField()
    description = models.TextField()
    genre = models.TextField(default='unknown')
    price = models.FloatField()
    is_on_sale = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

