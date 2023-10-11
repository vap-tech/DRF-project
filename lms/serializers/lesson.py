from rest_framework import serializers

from lms.models import Lesson
from lms.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('pk', 'name', 'course', 'preview', 'description', 'video_url',)
        validators = [UrlValidator(field='video_url')]


class LessonAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('pk', 'name', 'description', 'video_url',)
