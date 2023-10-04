from rest_framework import serializers

from lms.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('pk', 'name', 'course', 'preview', 'description', 'video_url',)


class LessonAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('pk', 'name', 'description', 'video_url',)
