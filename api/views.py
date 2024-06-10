from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,employee
from api.serializers import companyserializer,employeeserialixer
# Create your views here.
class companyviewset(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companyserializer


class employeeviewset(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=employeeserialixer