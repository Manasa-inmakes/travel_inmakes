from django.db import models

# # Create your models here.

class Place(models.Model):
   name=models.CharField(max_length=250)
   img=models.ImageField(upload_to='travels')
   des=models.TextField()
   def __str__(self):
         return self.name

class Port(models.Model):
     img=models.ImageField(upload_to='travels')

     def __str__(self):
         return str(self.img.name)

