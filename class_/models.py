from django.db import models
from Account.models import Account
from teacher.models import Teacher

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=10,null=True,blank=True)
    subject = models.CharField(max_length=100)
    code = models.CharField(max_length=10,unique=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
