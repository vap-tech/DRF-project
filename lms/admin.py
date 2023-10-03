from django.contrib import admin

from lms.models import Course, Lesson, Payment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'description',)
    ordering = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'preview', 'description', 'video_url',)
    list_filter = ('course',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'pay_date', 'course', 'lesson', 'amount', 'pay_method',)
    list_filter = ('user', 'pay_date', 'course', 'lesson', 'pay_method',)
