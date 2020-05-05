from django.db import models


# Create your models here.
class Product(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length=50)
	category = models.CharField(max_length=50, default="")
	subcategory = models.CharField(max_length=50, default="")
	price = models.IntegerField(default=0)
	description = models.CharField(max_length=5000)
	publish_Date = models.DateField()
	image = models.ImageField(upload_to="shop/images", default="")

	def __str__(self):  # function to represent the object in string
		return self.product_name


class Contact(models.Model):
	message_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, default="")
	email = models.CharField(max_length=50, default="")
	phone = models.CharField(max_length=50, default="")
	message = models.CharField(max_length=5000, default="")

	def __str__(self):  # function to represent the object in string
		return self.name
