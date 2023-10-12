from rest_framework import serializers

from lms.models import Course
from lms.serializers.lesson import LessonAllSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()
    lessons = LessonAllSerializer(source='lesson_set', many=True, read_only=True)  # разобраться до конца с фронтом

    def get_subscription(self, obj):
        request = self.context['request']
        return obj.subscription_set.filter(user=request.user).exists()

    @staticmethod
    def get_lesson_count(obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ('pk', 'name', 'preview', 'description', 'lesson_count', 'subscription', 'lessons')
