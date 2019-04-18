from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    btitle = models.CharField(max_length=255)
    bpub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hBook = models.ForeignKey('Bookinfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.hname

    def skill(self):
        return self.hcontent
    skill.short_description = "功夫"
