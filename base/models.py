from django.db import models
from django.core.validators import validate_email, MinLengthValidator, MinValueValidator, MaxValueValidator
from django.conf import settings

class Beneficiary(models.Model):

	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 40)
	dni = models.CharField(max_length = 9, unique = True)
	phone_number = models.IntegerField(null = True, blank = True)
	email = models.EmailField(unique = True, blank = True, validators=[validate_email])
	
	def __str__(self):
		return "{0} {1}".format(self.name, self.surname)

	def is_contactable(self):		
		return self.phone_number != None or self.email != ''

	is_contactable.admin_order_field = 'is_contactable'
	is_contactable.boolean = True
	is_contactable.short_description = 'Contactable'

class Worker(models.Model):

	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 40)
	dni = models.CharField(max_length = 9, unique = True)
	phone_number = models.IntegerField()
	email = models.EmailField(validators=[validate_email])
	category = models.CharField(max_length = 9, choices = (
			('E', 'Employee'),
			('V', 'Volunteer')
		))

	def __str__(self):
		return "[{0}] {1} {2}".format(self.category, self.name, self.surname)

class Donor(models.Model):

	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 40)
	dni = models.CharField(max_length = 9, unique = True)
	phone_number = models.IntegerField()
	email = models.EmailField(validators=[validate_email])	
	
	def __str__(self):
		return "{0} {1}".format(self.name, self.surname)

	def is_contactable(self):		
		return self.phone_number != None or self.email != ''

	is_contactable.admin_order_field = 'is_contactable'
	is_contactable.boolean = True
	is_contactable.short_description = 'Contactable'

class Product(models.Model):

	name = models.CharField(max_length = 30)
	description = models.TextField(blank = True)
	category = models.ForeignKey('ProductCategory')
	image = models.ImageField(upload_to = settings.IMAGES_ABS_URL, blank = True)

	def __str__(self):
		return "[{0}] {1}".format(self.category, self.name)

class ProductCategory(models.Model):

	name = models.CharField(max_length = 10, primary_key = True)

	def __str__(self):
		return self.name

class Donation(models.Model):

	date = models.DateTimeField(auto_now_add = True)
	donor = models.ForeignKey('Donor')
	money = models.DecimalField(max_digits = 7, decimal_places = 2)
	coin = models.ForeignKey('Coin')
	
	def __str__(self):
		return "[{0}] {1}".format(self.date, self.money)

class PeriodicalDonation(models.Model):

	initial_date = models.DateTimeField(auto_now_add = True)
	periodicity = models.PositiveIntegerField(null = True, validators = [
		MinValueValidator(1), MaxValueValidator(355)])
	money = models.DecimalField(max_digits = 7, decimal_places = 2)
	coin = models.ForeignKey('Coin')

class Coin(models.Model):

	acronym = models.CharField(max_length = 3, primary_key = True)
	name = models.CharField(max_length = 30)
	symbol = models.CharField(max_length = 1)