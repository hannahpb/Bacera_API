from django.shortcuts import render
from rest_framwork import viewsets
from .serializers import vehiclsSerializer
from .models import vehicls
# Create your views here.

class vehiclviewset(viewsets.ModelViewSet):
    query = vehicls.objects.all().order_by('name')
    serializer_class = vehiclsSerializer
    
