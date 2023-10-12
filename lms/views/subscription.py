from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from lms.models import Subscription
from lms.serializers.subscription import SubscriptionSerializer


class SubscriptionCreateView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        new_subscription = serializer.save()
        new_subscription.user = self.request.user
        new_subscription.save()


class SubscriptionDeleteView(DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, ]
