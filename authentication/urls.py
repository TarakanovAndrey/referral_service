from django.urls import path

from .views import RegistrationAPIView

app_name = 'authentication'
urlpatterns = [
    path('users/create', RegistrationAPIView.as_view()),
]