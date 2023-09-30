from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    preview = models.ImageField(upload_to='lesson', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

