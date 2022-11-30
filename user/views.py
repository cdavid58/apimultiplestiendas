from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .models import User

@api_view(['POST'])
def Login(request):
	data = request.data
	return Response({'result':User().Validate_Login(data['email'],data['psswd'])})

@api_view(['POST'])
def Register(request):
	return Response({'result':User().Register_User(request.data)})
