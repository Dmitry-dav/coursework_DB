from datetime import date

from django.db import models


# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length=50)
    date_of_foundation = models.DateTimeField()
    picture = models.ImageField()


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    date_of_foundation = models.DateTimeField()
    picture = models.ImageField()


class Game(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.CharField(max_length=255)
    likes_count = models.IntegerField()
    dislikes_count = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    image = models.ImageField()


# Добавить во все хуйхи всю хуйню
# Добавить комментарии
# Добавить лайки и дизлайки
# Добавить переход к отдельным сущностям
#хуй пизда хуй

