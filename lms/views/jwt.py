from rest_framework_simplejwt.views import TokenObtainPairView

from lms.serializers.jwt import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
