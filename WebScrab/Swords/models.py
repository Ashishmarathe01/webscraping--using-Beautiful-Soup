from django.db import models

# Create your models here


class Url(models.Model):
    ur = models.CharField(max_length=255,blank=False,unique=True)
    def __str__(self):
        return self.ur


class Words(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.word

