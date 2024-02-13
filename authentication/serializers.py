from rest_framework import serializers
from .models import CustomUser
from utils.utils import is_valid_email


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        email = data["email"]
        if not is_valid_email(email):
            raise Exception(f"You cannot create an account using the email "
                            f"address <{email}>, as it is not valid")
        return data

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
