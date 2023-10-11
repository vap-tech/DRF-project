from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from lms.models import Course
from lms.serializers.course import CourseSerializer
from lms.permission import IsOwnerOrManager


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrManager]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()
