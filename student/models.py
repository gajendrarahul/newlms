from django.db import models
from Account.models import Account

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=200,default='98********')
    profile = models.ImageField(blank=True,null=True,upload_to='profile/')
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
