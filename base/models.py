# -*- encoding: utf-8 -*-

from django.db import models
from django.core.validators import validate_email, MinLengthValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.conf import settings

class Person(models.Model):

	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 40)
	dni = models.CharField(max_length = 9, unique = True)
	phone_number = models.IntegerField(null = True, blank = True)
	email = models.EmailField(unique = True, null = True, blank = True)
	category = models.CharField(max_length = 9, choices = (
			('E', 'Employee'),
			('V', 'Volunteer'),
			('B', 'Beneficiary')
		))

	def save(self, *args, **kwargs):
	    self.email = self.email.lower().strip()
	    if self.email != "":
	        validate_email(self.email)
	    else:
	        self.email = None
	    super(Person, self).save(*args, **kwargs)

	def is_contactable(self):		
		return self.phone_number != None or self.email != None

	is_contactable.admin_order_field = 'is_contactable'
	is_contactable.boolean = True
	is_contactable.short_description = 'Contactable'

	def __unicode__(self):
		return u"[{0}] {1} {2}".format(self.category, self.name, self.surname)
	

class Product(models.Model):

	name = models.CharField(max_length = 30)
	description = models.TextField(blank = True)
	category = models.ForeignKey('ProductCategory')
	image = models.ImageField(upload_to = settings.IMAGES_ABS_URL, blank = True)

	def __unicode__(self):
		return u"[{0}] {1}".format(self.category, self.name)

class ProductCategory(models.Model):

	name = models.CharField(max_length = 10, primary_key = True)

	def __unicode__(self):
		return unicode(self.name)

class Donation(models.Model):

	donor = models.ForeignKey('Person')
	date = models.DateTimeField(auto_now_add = True)
	money = models.DecimalField(max_digits = 7, decimal_places = 2)
	coin = models.ForeignKey('Coin')
	periodical_donation = models.ForeignKey('PeriodicalDonation', null = True, blank = True)

	def is_instance_of_periodical(self):
		return self.periodical_donation != None

	is_instance_of_periodical.admin_order_field = 'is_instance'
	is_instance_of_periodical.boolean = True
	is_instance_of_periodical.short_description = 'Periodical'
	
	def __unicode__(self):
		return u"[{0}] {1}{2}".format(self.date, self.money, self.coin)

class PeriodicalDonation(models.Model):

	donor = models.ForeignKey('Person')
	initial_date = models.DateTimeField(auto_now_add = True)
	periodicity = models.PositiveIntegerField(null = True, validators = [
		MinValueValidator(1), MaxValueValidator(355)])
	money = models.DecimalField(max_digits = 7, decimal_places = 2)
	coin = models.ForeignKey('Coin')

	def __unicode__(self):
		return u"{0} donate {1}{2} each {3} days".format(
			self.donor, self.money, self.coin, self.periodicity)

class Coin(models.Model):

	acronym = models.CharField(max_length = 3, primary_key = True)
	name = models.CharField(max_length = 30)
	symbol = models.CharField(max_length = 1, blank = True)

	def __unicode__(self):
		return unicode(self.symbol) if (self.symbol != '') else unicode(self.acronym)