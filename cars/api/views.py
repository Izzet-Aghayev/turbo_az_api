from wsgiref import headers
from rest_framework import status, generics
from rest_framework.response import Response

from ..models import Announcement, AnnouncementImage
from .serializers import (
    CreateAnnouncementSerializer,
)



class CreateAnnouncementAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = CreateAnnouncementSerializer

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        announcement = serializer.save()

        for image in images:
            AnnouncementImage.objects.create(announcement=announcement, image=image)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
