
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import models, serializers

class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()