from django.shortcuts import render
from rest_framework.response import Response 

# Create your views here.
def add_user(request):
    name = request.data.get('name')
    age = request.data.get('age')
    last = request.data.get('last')
    name_obj = Name.objects.create(name=name,age=age)
    return Response('Success')

