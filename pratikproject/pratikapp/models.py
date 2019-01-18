from django.db import models







class Task(models.Model):
    taskname=models.CharField(max_length=30)
    deadline=models.DateField()
    completed=models.BooleanField()
