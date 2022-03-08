from pyexpat import model
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.

class Reservation(models.Model):
    """ Make a reservation """
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True)
    def __str__(self):
        return self.name

class announcement(models.Model):
    """ Make a announcement """
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'announcements'
    def __str__(self):
        return self.text[:50]

