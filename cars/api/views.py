from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Announcement
from .serializers import (
    CreateSerializer,
)



class CreateAnnouncementAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = CreateSerializer
