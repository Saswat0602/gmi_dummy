import uuid
from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.conf import settings

class EmailToken(models.Model):
    EMAIL_VERIFICATION = 'email_verification'
    PASSWORD_RESET = 'password_reset'

    TOKEN_TYPE_CHOICES = [
        (EMAIL_VERIFICATION, 'Email Verification'),
        (PASSWORD_RESET, 'Password Reset'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='email_tokens')
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    token_type = models.CharField(max_length=50, choices=TOKEN_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() < self.created_at + timedelta(hours=24)

    def __str__(self):
        return f"{self.user.email} - {self.token_type}"
