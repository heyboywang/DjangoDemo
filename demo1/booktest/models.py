from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    btitle = models.CharField(max_length=255)
    bpub_date = models.DateTimeField()

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hBook = models.ForeignKey('Bookinfo',on_delete=models.CASCADE)
