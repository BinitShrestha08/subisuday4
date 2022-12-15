from django.shortcuts import render
from rest_framework import viewsets
from api.models import OLT
from api.serializers import OltSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from scripts import *
# from scripts import logstotxt
# Create your views here.

class OltViewset(viewsets.ModelViewSet):
    queryset=OLT.objects.all()
    serializer_class = OltSerializer
   

