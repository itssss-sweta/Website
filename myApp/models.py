
from django.db import models

#Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()


    def __str__(self):
        return self.name
class Topics(models.Model):
    top_name=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.name
class Webpage(models.Model):
    topic=models.ForeignKey(Topics,models.CASCADE)
    name=models.CharField(max_length=122)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)

