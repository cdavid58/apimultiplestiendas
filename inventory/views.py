from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from dotenv import load_dotenv
from .models import *
import os

load_dotenv()

@api_view(['POST'])
def Save_Category(request):
	Category(
		name = request.data['name']
	).save()
	return Response({'result':True})


@api_view(['POST'])
def Save_SubCategory(request):
	SubCategories(
		name = request.data['name'],
		category = Category.objects.get(pk = request.data['id_category'])
	).save()
	return Response({'result':True})


@api_view(['POST'])
def GET_LIST_SUBCATEGORIES(request):
	data = request.data
	cat = Category.objects.get(pk = data['pk_category'])
	data = [
		{
			"name":i.name,
			"img":os.getenv("URL_IMG")+i.img.url,
			'pk':i.pk
		}
		for i in SubCategories.objects.filter(category = cat )
	]
	n = cat.searched + 1
	cat.searched = n
	cat.save()
	return Response(data)


@api_view(['POST'])
def GET_CATEGORY_MORE_SEARCHED(request):
	data = [
		{
			'name':i.name,
			'img':os.getenv('URL_IMG')+i.img.url
		}
		for i in Category.objects.all().exclude(searched = 0).order_by('-searched')[:10]
	]
	return Response(data)


@api_view(['POST'])
def GET_ALL_CATEGORIES(request):
	data = [
		{
			'name':i.name,
			'img':os.getenv('URL_IMG')+i.img.url,
			'pk':i.pk
		}
		for i in Category.objects.all()
	]
	return Response(data)

@api_view(['POST'])
def GET_LIST_INVENTORY(request):
	data = request.data
	product = Product.objects.filter(company = Company.objects.get(pk = data['company']))
	data = [
		{
			"name":i.name,
			"price":i.price,
			"img":os.getenv('URL_IMG')+i.img.url,
			"pk":i.pk
		}
		for i in product
	]
	return Response(data)

@api_view(['POST'])
def CREATE_PRODUCT(request):
	data = request.data
	Product(
		name = data['name'],
		price = data['price'],
		tax = data['tax'],
		quanty = data['quanty'],
		description = data['description'],
		shipping = data['shipping'],
		company = Company.objects.get(pk = data['company']),
		subcategories = SubCategories.objects.get(pk = data['subcategories']),
		img = data['img']
	).save()
	return Response({'result':True})

@api_view(['POST'])
def LIST_PRODUCTS(request):
	data = request.data
	list_product = Product.objects.filter(subcategories = data['subcategory'])
	if data['price_low'] is not None:
		list_product = Product.objects.filter(subcategories = data['subcategory'], price__lte = data['price_top'], price__gte = data['price_low'] )

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
		for i in list_product
	]
	return Response(data)