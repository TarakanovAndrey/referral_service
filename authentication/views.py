from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from drfasyncview import AsyncAPIView
from django.http import JsonResponse
from asgiref.sync import sync_to_async


class RegistrationAPIView(AsyncAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    @sync_to_async
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
