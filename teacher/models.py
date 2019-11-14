from django.db import models
from Account.models import Account

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    department = models.CharField(max_length=100, blank=True,null=True)
    contact = models.IntegerField(default=None)
    address = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile/')
    subject = models.BooleanField(max_length=200,blank=True,null=True)
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    def __str__(self):
        return self.name