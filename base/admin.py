from django.contrib import admin
from base.models import Beneficiary, Worker, Product, ProductCategory


class BeneficiaryAdmin(admin.ModelAdmin):
	fieldsets = [
		("Campos obligatorios", {'fields': ('name', 'surname', 'dni')}),
		("Campos opcionales", {'fields': ('phone_number', 'email')})
	]
	search_fields = ('name', 'surname', 'dni', 'phone_number', 'email')
	list_display = ('name', 'surname', 'is_contactable')

class WorkerAdmin(admin.ModelAdmin):
	list_filter = ['category']
	search_fields = ('name', 'surname', 'dni', 'phone_number', 'email')
	list_display = ('name', 'surname', 'category')

## TODO 
# Show image preview in form
class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		("Campos obligatorios", {'fields': ('name', 'category')}),
		("Campos opcionales", {'fields': ('description', 'image')})
	]
	list_filter = ['category']
	search_fields = ['name']
	list_display = ('name', 'category')

admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
