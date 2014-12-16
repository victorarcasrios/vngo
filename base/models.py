from django.db import models
from django.core.validators import validate_email, MinLengthValidator

class Person(models.Model):

	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 40)
	dni = models.CharField(max_length = 9, unique = True)
	phone_number = models.IntegerField(null = True)
	email = models.EmailField(unique = True, blank = True, validators=[validate_email])
	category = models.CharField(max_length = 11, choices = (
			('B', 'Beneficiary'),
			('E', 'Employee'),
			('V', 'Volunteer')
		))

	def __str__(self):
		return "[{0}] {1} {2}".format(self.category, self.name, self.surname)