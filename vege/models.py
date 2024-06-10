from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    # pass
    receipname=models.CharField(max_length=100,null=True)
    receipdes=models.TextField(default="")
    image=models.ImageField(upload_to="receipe",default="")
    # receip=models.CharField(max_length=100,null=True)
    

