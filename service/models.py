from django.db import models
from authentication.models import CustomUser


class ReferralCode(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.TextField(max_length=20, blank=True, unique=True)
    created_at = models.DateField(auto_now_add=True)
    valid_until = models.DateField(blank=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Referrer(models.Model):
    email = models.EmailField(max_length=200)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email', 'code'], name='unique_fields')
        ]

    def __str__(self):
        return self.pk
