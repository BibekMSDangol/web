from django.db import models

# Create your models here.

class Guitar(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    guitar_type=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=200)
    image=models.FileField(upload_to='guitar',default="guitar.jpg")
    

    class Meta:
        db_table="guitar"