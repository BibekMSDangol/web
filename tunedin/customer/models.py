
from django.db import models

class Customer(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    customer_firstname=models.CharField(max_length=100)
    customer_lastname=models.CharField(max_length=100)
    customer_email=models.CharField(max_length=200)
    customer_phone=models.CharField(max_length=10)
    customer_password=models.CharField(max_length=100)

    class Meta:
        db_table="customer"





# Create your models here.
