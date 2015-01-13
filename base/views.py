from django.shortcuts import render
from django.http import HttpResponse
from models import Product

def index(request):
	return HttpResponse("Welcome VNGO")

def objects_list(request, category_id = None):
	if category_id == None:
		objects = Product.objects.all()
	else:
		## ERROR
		objects = Product.objects.filter(category__id = category_id)

	output = "<p>Categoria {0}</p><ul>".format(category_id)
	for obj in objects:
		output += "<li>{0}</li>".format(obj.name)
	return HttpResponse(output + "</ul>")

def object_detail(request, object_id):
	return HttpResponse("Object detail #{0}".format(object_id))