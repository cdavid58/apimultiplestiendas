from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from dotenv import load_dotenv
from .models import *
import os

@api_view(['POST'])
def GET_LIST_PRODUCT_BY_COMPANY(request):
	data = request.data
	product = Product.objects.filter(company = Company.objects.get(pk = data['company']))
	data = [
		{
			"name":i.name,
			"img":os.getenv('URL_IMG')+i.img.url,
			"pk":i.pk,
			'price':i.price,
			'features':[
				{
					'color' : Features.objects.get(product = i).color,
					'size' : Features.objects.get(product = i).size,
					'state' : Features.objects.get(product = i).state,
					'marca' : Features.objects.get(product = i).marca,
					'modelo' : Features.objects.get(product = i).modelo,
					'unidades_por_pack' :Features.objects.get(product = i).unidades_por_pack
				}
			]
		}
		for i in product
	]
	print(data)
	return Response(data)

from django.forms.models import model_to_dict

@api_view(['POST'])
def GET_DETAIL_PRODUCT(request):
	data = request.data
	product = Product.objects.get(pk = data['product'])
	features = Features.objects.get(product = product)
	g = Gallery.objects.get(product = product)
	data = {}
	data['product'] = {
		'pk_company':product.company.pk,
		"name":product.name,
		"img":os.getenv('URL_IMG')+product.img.url,
		"pk":product.pk,
		'quanty':product.quanty,
		'price':product.price,
		'description':product.description,
		'shipping':product.shipping,
		'color' : features.color,
		'size' : features.size,
		'state' : features.state,
		'marca' : features.marca,
		'modelo' : features.modelo,
	}
	data['gallery'] = []
	if g.img_1 != "":
		data['gallery'].append({'img':os.getenv('URL_IMG')+g.img_1.url})
	if g.img_2 != "":
		data['gallery'].append({'img':os.getenv('URL_IMG')+g.img_1.url})
	if g.img_3 != "":
		data['gallery'].append({'img':os.getenv('URL_IMG')+g.img_3.url})
	if g.img_4 != "":
		data['gallery'].append({'img':os.getenv('URL_IMG')+g.img_4.url})
	if g.img_5 != "":
		data['gallery'].append({'img':os.getenv('URL_IMG')+g.img_5.url})
	return Response(data)