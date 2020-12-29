from django.db import models

# Create your models here.
class Kawasaki(models.Model):
   kawasaki_id = models.AutoField(auto_created=True, primary_key=True)
   model = models.CharField(max_length=100,default='')
   price = models.CharField(max_length=100,default='')
   description = models.CharField(max_length=100)
   image = models.FileField(upload_to="images/kawasaki/")

   class Meta:
       db_table = "kawasaki"
