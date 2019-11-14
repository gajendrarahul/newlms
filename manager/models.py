from django.db import models
from Account.models import Account

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100,null=True,blank=True,default='98xxxxxxxx')
    designation = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='profile/',null=True,blank=True)
    user = models.OneToOneField(Account,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name