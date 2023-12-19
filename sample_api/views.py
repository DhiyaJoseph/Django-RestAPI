from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import person
from .serializers import PersonSerializer

class PersonListCreateView(ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer
