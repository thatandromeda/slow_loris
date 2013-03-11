from django.db import models

class Intro(models.Model):
    text = models.CharField(max_length=50)

class Suggestion(models.Model):
    text = models.CharField(max_length=140)
    link = models.URLField()
    flag = models.IntegerField(default=0)
    
class Picture(models.Model):
    image_link = models.URLField()
    attribution = models.CharField(max_length=140)
    attribution_link = models.URLField()