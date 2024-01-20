from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer
# Create your views here.

# Generics Views for API :-
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer



# Normal URL views:-
def home(request):
    return HttpResponse("Hello, CodeSnippers")
