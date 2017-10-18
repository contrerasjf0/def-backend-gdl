# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Luages
from .serializers import LugaresSerializer
from django.shortcuts import render
from lugares.models import *

# Create your views here.

class LugaresApi(APIView):

	def get(self, request):
		lugares = Lugares.objects.all()
		serializer = LugaresSerializer(lugares, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = LugaresSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
