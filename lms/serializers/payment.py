from rest_framework import serializers

from lms.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('pk', 'user', 'pay_date', 'course', 'lesson', 'amount', 'pay_method',)
