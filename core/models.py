from django.db import models

# Create your models here.

class User(models.Model):

   first_name = models.CharField(max_length = 50)   
   last_name = models.CharField(max_length = 50)
   email = models.EmailField(max_length=254)
   password = models.CharField(max_length = 50)
   is_active = models.BooleanField(default=True)
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now=True)

