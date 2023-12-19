from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import person
from .serializers import PersonSerializer

class PersonListCreateView(ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer

class personDetailAPIview(RetrieveUpdateDestroyAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer
