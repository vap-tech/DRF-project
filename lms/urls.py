from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from lms.apps import LmsConfig
from lms.views.course import CourseViewSet
from lms.views.jwt import MyTokenObtainPairView
from lms.views.lesson import LessonCreateView, LessonListView, LessonDetailView, LessonUpdateView, LessonDeleteView
from lms.views.payment import PaymentListView

app_name = LmsConfig.name

urlpatterns = [
    path('lesson/create/', LessonCreateView.as_view()),
    path('lesson/all/', LessonListView.as_view()),
    path('lesson/<int:pk>/', LessonDetailView.as_view()),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view()),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view()),

    path('payment/all/', PaymentListView.as_view()),

    path('token/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

course_router = routers.DefaultRouter()
course_router.register('course', CourseViewSet)

urlpatterns += course_router.urls
