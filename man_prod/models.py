from django.db import models

# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length = 50)

class Product(models.Model):

   product_name = models.CharField(max_length = 50)
   image = models.ImageField(upload_to = 'static/images/',blank=True,help_text="not found")
   category = models.CharField(max_length = 50)
   description = models.TextField()
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now=True)
