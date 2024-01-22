from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
# Create your views here.

# Generics Views for API :-
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):  # new
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class UserList(generics.ListAPIView):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Normal URL views:-
def home(request):
    return HttpResponse("Hello, CodeSnippers")

@api_view(['GET'])
def api_root(request, format=None):

    return Response(
        {
            "users": reverse('user-list', request=request, format=format),
            "snippets": reverse('snippet-list', request=request, format=format),
        }
    )