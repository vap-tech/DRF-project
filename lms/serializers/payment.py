from rest_framework import serializers

from lms.models import Payment, Course
from lms.services import get_pay_url


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('pk', 'user', 'pay_date', 'course', 'lesson', 'amount', 'pay_method',)


class PaymentCreateSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    @staticmethod
    def get_status(obj):
        return 'OK'

    def get_url(self, obj):
        request = self.context['request']

        course_id = request.data['course']
        amount = request.data['amount']

        course_name = Course.objects.filter(pk=course_id).first().name

        pay_url = get_pay_url(course_name, amount)

        return [pay_url, ]

    class Meta:
        model = Payment
        fields = ('course', 'amount', 'status', 'url',)
