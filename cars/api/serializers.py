from rest_framework import serializers

from ..models import (
    Announcement,
)


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ('created_at', 'updated_at')
