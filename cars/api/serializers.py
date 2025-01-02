from rest_framework import serializers

from ..models import (
    Announcement,
    AnnouncementImage,
)


class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ('image',)


class CreateAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ('created_at', 'updated_at')
