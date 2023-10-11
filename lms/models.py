from django.db import models

from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    owner = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    preview = models.ImageField(upload_to='lesson', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    owner = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):

    PAY_CHOICES = [
        ('cash', 'наличные'),
        ('card', 'карта'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    pay_date = models.DateTimeField(verbose_name='дата оплаты', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    pay_method = models.CharField(choices=PAY_CHOICES, verbose_name='способ оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.user}//{self.course if self.course else self.lesson}//{self.pay_date}//{self.amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('user', 'course', 'lesson')


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)

    def __str__(self):
        return f'{self.user} подписан на {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        ordering = ('user', 'course')
