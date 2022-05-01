
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .models import CustomUser

from authapp.serializers import SignUpSerializer

class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = SignUpSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SignUpSerializer(user)
        return Response(serializer.data)

