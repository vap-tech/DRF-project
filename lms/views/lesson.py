from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from lms.models import Lesson
from lms.serializers.lesson import LessonSerializer
from lms.permission import IsOwner, IsManager
from lms.paginators import LmsPagination


class LessonCreateView(CreateAPIView):
    """ Lesson create endpoint """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListView(ListAPIView):
    """ Lesson list endpoint """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsManager]
    pagination_class = LmsPagination


class LessonDetailView(RetrieveAPIView):
    """ Lesson detail endpoint """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonUpdateView(UpdateAPIView):
    """ Lesson update endpoint """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDeleteView(DestroyAPIView):
    """ Lesson delete endpoint """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]
