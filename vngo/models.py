from django.db import models

class Product(models.Model):
	product_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)