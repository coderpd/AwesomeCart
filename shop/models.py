from django.db import models


# Create your models here.
class Product(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length=50)
	discription = models.CharField(max_length=300)
	publish_Date = models.DateField()
