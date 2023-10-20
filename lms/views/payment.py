from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView

from lms.models import Payment
from lms.serializers.payment import PaymentSerializer, PaymentCreateSerializer


class PaymentListView(ListAPIView):
    """ Payment list endpoint"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('course', 'lesson', 'pay_method',)
    ordering_fields = ('pay_date',)


class PaymentCreateView(CreateAPIView):
    """ Payment create endpoint """
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer
