from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)          # название фильма
    description = models.TextField()                  # описание фильма
    review = models.TextField()                       # отзыв

    def __str__(self):
        return self.title

