from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    c_id = models.CharField(max_length=5 , primary_key=True)
    c_name = models.CharField(max_length=64)
    
    semestry_choices = [("1","1"),("1","2"),]
    
    semestry = models.CharField(max_length = 5, choices = semestry_choices, default = "")
    year = models.PositiveIntegerField()
    vacancy = models.PositiveIntegerField()
    
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'
    status_choices = [('OPEN','OPEN'),('CLOSE','CLOSE')]
    
    status = models.CharField(max_length = 5, choices = status_choices, default = "CLOSE")
    students = models.ManyToManyField(User, blank=True, related_name="course")
    
    def __str__(self):
        return f"Course ID: {self.c_id}, Name:{self.c_name}"
        

