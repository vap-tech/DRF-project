from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from lms.models import Course
from lms.serializers.course import CourseSerializer
from lms.permission import IsOwner, IsManager
from lms.paginators import LmsPagination
from lms.tasks import send_info


class CourseViewSet(ModelViewSet):
    """ Course endpoint """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsManager]
    pagination_class = LmsPagination

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        update_course = serializer.save()
        send_info.delay(update_course)
        update_course.save()
