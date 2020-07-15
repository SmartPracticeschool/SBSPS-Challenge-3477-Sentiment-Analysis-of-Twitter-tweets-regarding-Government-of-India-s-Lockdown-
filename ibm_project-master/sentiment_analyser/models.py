from django.db import models
#from phone_field import PhoneField

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(blank = True)
    contact_number = models.CharField(max_length=10)
