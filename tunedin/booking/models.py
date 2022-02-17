from django.db import models

class Booking(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=200)

    class Meta:
        db_table="booking"
