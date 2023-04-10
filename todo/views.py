from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import TodoSerializer

from .models import Todo


class TodoView(viewsets.ModelViewSet):

    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = TodoSerializer

    # define a variable and populate it
    # with the Todo list objects
    queryset = Todo.objects.all()
