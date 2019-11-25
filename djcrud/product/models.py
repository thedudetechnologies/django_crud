from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):

   cat_name = models.CharField(max_length = 50 , blank=False,null=False)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now=True)
   updated = models.DateTimeField(auto_now=True)




class Product(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product_name = models.CharField(max_length = 50)
   image = models.ImageField(upload_to = 'images/',blank=True,help_text="not found")
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   description = models.TextField()
   created = models.DateTimeField(auto_now=True)
   updated = models.DateTimeField(auto_now=True)
