from django.db import models

# Create your models here.

class clarification(models.Model):
    """ Model to represent an incoming clarification"""
    my_message = models.TextField()
    

class time(models.Model):
    """Model used to manage the time the proctored event needs to take"""
    hours = models.IntegerField()
    minutes = models.IntegerField()
    start_time = models.IntegerField()

