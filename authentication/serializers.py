from rest_framework import serializers
from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    # """ Сериализация регистрации пользователя и создания нового. """
    #
    # # Убедитесь, что пароль содержит не менее 8 символов, не более 128,
    # # и так же что он не может быть прочитан клиентской стороной
    # password = serializers.CharField(
    #     max_length=128,
    #     min_length=8,
    #     write_only=True
    # )
    # id = serializers.IntegerField()
    #
    # # Клиентская сторона не должна иметь возможность отправлять токен вместе с
    # # запросом на регистрацию. Сделаем его доступным только на чтение.


    class Meta:
        model = CustomUser
        # Перечислить все поля, которые могут быть включены в запрос
        # или ответ, включая поля, явно указанные выше.
        fields = ['id', 'email']

    def create(self, validated_data):
        # Использовать метод create_user, который мы
        # написали ранее, для создания нового пользователя.
        return CustomUser.objects.create_user(**validated_data)