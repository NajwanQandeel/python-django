from django.shortcuts import render
from rest_framework import generics   # for post and get 
from category.models import Category
from category.serilize import CategorySerializer
# Create your views here.

class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



