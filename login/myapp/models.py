from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.TextField()
    last_name=models.TextField()
    email=models.EmailField()
    mobile=models.IntegerField()
    password=models.CharField(max_length=12)
    cfmpwd=models.CharField(max_length=12)
    date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='images/',null=True)

