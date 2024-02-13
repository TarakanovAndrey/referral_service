from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser


class CustomUserTests(APITestCase):
    def test_create_user(self):
        url = reverse_lazy('authentication:user-create')
        data = {
            "user": {"email": "email_test@yandex.ru",
                     "password": "password1"}
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, "email_test@yandex.ru")
