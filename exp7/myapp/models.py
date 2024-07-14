from django.db import models

class Student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    sem = models.IntegerField()

    def __str__(self):
        return f"{self.usn} {self.name} {self.sem}"

class Project(models.Model):
    studentname = models.CharField(max_length=200)
    ptopic = models.CharField(max_length=200)
    planguages = models.CharField(max_length=200)  # Corrected typo from 'plangauges'
    pduration = models.IntegerField(help_text='Enter in days')

    def __str__(self):
        return self.ptopic
