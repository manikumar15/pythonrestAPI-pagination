from django.shortcuts import render
from .serializers import EmpSerializer
from .models import Emp
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
	page_size = 3
	page_query_param = 'mypage' #which page u want to open 
	page_size_query_param = 'num'
	max_page_size = 5
	last_page_strings = ('endpage',)

class EmpViewset(ModelViewSet):
	queryset = Emp.objects.all()
	serializer_class = EmpSerializer
	pagination_class = MyPagination