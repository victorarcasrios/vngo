# -*- encoding: utf-8 -*-

from django.contrib import admin
from base.models import Person, Product, ProductCategory, Donation, PeriodicalDonation, Expense, Coin

## TODO 
# Show image preview in form

class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		("Campos obligatorios", {'fields': ('name', 'surname', 'dni', 'category')}),
		("Campos opcionales", {'fields': ('phone_number', 'email')})
	]
	list_filter = ['category']
	search_fields = ('name', 'surname', 'dni', 'phone_number', 'email')
	list_display = ('name', 'surname', 'is_contactable')

class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		("Campos obligatorios", {'fields': ('name', 'category')}),
		("Campos opcionales", {'fields': ('description', 'image')})
	]
	list_filter = ['category']
	search_fields = ['name']
	list_display = ('name', 'category')

class DonationAdmin(admin.ModelAdmin):
	search_fields = ('donor', 'date')
	list_display = ('date', 'donor', 'money', 'coin', 'is_instance_of_periodical')

class PeriodicalDonationAdmin(admin.ModelAdmin):
	list_filter = ['periodicity']
	search_fields = ['donor']
	list_display = ('donor', 'money', 'coin', 'periodicity')

class ExpenseAdmin(admin.ModelAdmin):
	list_filter = ['date']
	search_fields = ['subject']
	list_display = ('date', 'subject', 'money', 'coin')

admin.site.register(Person, PersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Donation, DonationAdmin)
admin.site.register(PeriodicalDonation, PeriodicalDonationAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Coin)
