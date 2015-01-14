from django.shortcuts import render
from django.http import HttpResponse
from models import Product, ProductCategory

def index(request):
	return HttpResponse("Welcome VNGO")

def objects_list(request, category_name = None):
	if category_name == None:
		objects = Product.objects.all()
	else:
		category = ProductCategory.objects.get(name = category_name)
		objects = Product.objects.filter(category = category)

	output = "<p>Categoria {0}</p><ul>".format(category_name)
	for obj in objects:
		output += "<li>{0}</li>".format(obj.name)
	return HttpResponse(output + "</ul>")

def object_detail(request, object_id):
	return HttpResponse("Object detail #{0}".format(object_id))