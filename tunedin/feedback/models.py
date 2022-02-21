
from email import message
from django.db import models

class Feedback(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    email=models.CharField(max_length=200)
    need=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)

    class Meta:
        db_table="feedback"


