from django.db import models

# Create your models here.
class Employee(models.Model):
    employeeid = models.AutoField(primary_key=True)  
    employeename = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.employeename
