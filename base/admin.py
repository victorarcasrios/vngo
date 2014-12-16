from django.contrib import admin
from base.models import Person

class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		("Campos obligatorios", {'fields': ['name', 'surname', 'dni', 'category']}),
		("Campos opcionales", {'fields': ['phone_number', 'email']})
	]

admin.site.register(Person, PersonAdmin)
