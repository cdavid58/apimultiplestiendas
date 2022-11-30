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
def GET_LOGO_COMPANY(request):
	data = [
		{
			'pk':i.pk,
			'img':os.getenv('URL_IMG')+i.logo.url
		}
		for i in Company.objects.all()
	]
	return Response(data)

