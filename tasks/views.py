# from django.shortcuts import render
from rest_framework import viewsets
from tasks.serializer import TaskSerializer
from .models import task

# Create your views here.
class taskView(viewsets.ModelViewsets):
    serialzer_class = TaskSerializer
    queryset = task.objects.all()