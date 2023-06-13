from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import random
import string


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('courier', 'courier'),
        ('sender', 'sender'),
        ('drop_pick_zone', 'drop_pick_zone'),
    )
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('on-trip', 'On Trip'),
    )
    name = models.CharField(max_length=20, null=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='role', null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.username


class Package(models.Model):
    STATUS_CHOICES = (
        ('upcoming', 'upcoming'),
        ('dropped_off', 'dropped_off'),
        ('ongoing', 'ongoing'),
        ('arrived', 'arrived'),
        ('completed', 'completed'),
    )
    DELIVERY_CHOICES =(
        ('standard', 'standard'),
        ('premium', 'premium'),
        ('express', 'express'),
    )

    PACKAGE_PREFIX = 'pn'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages', null=True)
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assigned_packages', null=True, blank=True)
    packageName = models.CharField(max_length=100)
    deliveryType = models.CharField(max_length=20, choices=DELIVERY_CHOICES)
    dropOffLocation = models.ForeignKey(User, on_delete=models.CASCADE)
    packageDescription = models.TextField()
    recipientName = models.CharField(max_length=100)
    recipientEmail = models.CharField(max_length=100)
    recipientTelephone = models.CharField(max_length=100)
    recipientAddress = models.CharField(max_length=200)
    sendersAddress = models.CharField(max_length=200)
    package_number = models.CharField(max_length=7, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_at = models.DateTimeField(null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)


    def __str__(self):
        return self.packageName

    def save(self, *args, **kwargs):
        if self.courier is None and self.status == 'ongoing':
            raise ValueError("Courier must be assigned for packages with 'ongoing' status.")      
        if not self.package_number:
            self.package_number = self._package_package_number()
        if self.courier:
                self.assigned_at = timezone.now()
        super().save(*args, **kwargs)

    def _package_package_number(self):
        digits = ''.join(random.choices(string.digits, k=5))
        return f'{self.PACKAGE_PREFIX}{digits}'

