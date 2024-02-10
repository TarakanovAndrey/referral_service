from rest_framework import serializers
from .models import ReferralCode, Referrer
from service.utils import generates_code
from django.shortcuts import get_object_or_404


class ReferralCodeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner_id = serializers.IntegerField()
    code = serializers.CharField(max_length=20, read_only=True)
    created_at = serializers.DateField(read_only=True)
    valid_until = serializers.DateField()
    is_active = serializers.BooleanField(default=False)

    def create(self, validated_data):
        code = generates_code()
        validated_data['code'] = code
        if validated_data['is_active']:
            ReferralCode.objects.filter(owner_id=validated_data['owner_id']).update(is_active=False)
        return ReferralCode.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data['is_active']:
            ReferralCode.objects.filter(owner_id=instance.owner_id).update(is_active=False)

        for field in validated_data:
            setattr(instance, field, validated_data[field])

        instance.save()
        return instance


class ReferrerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    code_value = serializers.CharField(write_only=True)
    owner_id = serializers.IntegerField(read_only=True)
    code_id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateField(read_only=True)

    def create(self, validated_data):
        code_value = validated_data['code_value']
        code_obj = get_object_or_404(ReferralCode, code=code_value)
        owner_id = code_obj.owner_id
        code_id = code_obj.id

        del validated_data['code_value']

        validated_data["owner_id"] = owner_id
        validated_data["code_id"] = code_id


        return Referrer.objects.create(**validated_data)
