from django.db import models

# Create your models here.

#create company model
class company(models.Model):
    companyid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('NON IT','NON IT'),("MOBILE PHONES","MOBILE PHONES")))
    addeddate=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name+'--'+self.location


# create employee api
class employee(models.Model):
    employeid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    emailid=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(('manager','manager'),('sde','sde'),('project lead','pl')))

    companyy=models.ForeignKey(company,on_delete=models.CASCADE)