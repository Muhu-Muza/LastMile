from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
import random
import string
from django.core.exceptions import ValidationError


class CustomUserManager(UserManager):
    def create_admin(self, username, password):
        admin = self.create_user(username=username, password=password)
        admin.is_staff = True
        admin.is_superuser = True
        admin.role = 'admin'
        admin.save()
        return admin

class Warehouse(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=20, null=True, blank=True)
    tag = models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return self.name

class DropPickZone(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=20, null=True, blank=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='drop_pick_zones')
    tag = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('courier', 'Courier'),
        ('sender', 'Sender'),
        ('drop_pick_zone', 'Drop/Pick Zone'),
        ('warehouse', 'Warehouse'),
    )
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('on-trip', 'On Trip'),
    )
    name = models.CharField(max_length=40, null=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Role', null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    objects = CustomUserManager()

    # Add warehouse-specific fields
    tag = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    drop_pick_zone = models.ForeignKey(DropPickZone, related_name='users', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    # Add drop_pick_zone-specific fields
    warehouse = models.ForeignKey(Warehouse, related_name='users', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username





class Package(models.Model):
    STATUS_CHOICES = (
        ('upcoming', 'Upcoming'),
        ('dropped_off', 'Dropped Off'),
        ('dispatched', 'Dispatched'),
        ('en_route', 'En Route'),
        ('warehouse_arrival', 'Warehouse Arrival'),
        ('in_house', 'In House'),
        ('in_transit', 'In Transit'),
        ('at_pickup', 'At Pickup'),
        ('ready_for_pickup', 'Ready for Pickup'),
        ('pending_delivery', 'Pending Delivery'),
        ('out_for_delivery', 'Out for Delivery'),
        ('ongoing', 'Ongoing'),
        ('arrived', 'Arrived'),
        ('completed', 'Completed'),
    )
    DELIVERY_CHOICES = (
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('express', 'Express'),
    )

    PACKAGE_PREFIX = 'pn'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages', null=True)
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assigned_packages', null=True, blank=True)
    packageName = models.CharField(max_length=100)
    deliveryType = models.CharField(max_length=20, choices=DELIVERY_CHOICES)
    dropOffLocation = models.ForeignKey(DropPickZone, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='packages_dropped_off')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True, related_name='packages_in_house')
    packageDescription = models.TextField()
    recipientName = models.CharField(max_length=100)
    recipientEmail = models.CharField(max_length=100)
    recipientTelephone = models.CharField(max_length=100)
    recipientAddress = models.CharField(max_length=200)
    sendersAddress = models.CharField(max_length=200)
    package_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')  # default status is 'upcoming'
    created_at = models.DateTimeField(default=timezone.now)
    assigned_at = models.DateTimeField(default=timezone.now)
    otp = models.CharField(max_length=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.package_number:
            self.package_number = self.generate_package_number()

        if self.status in ['dropped_off', 'in_house', 'ready_for_pickup']:
            if self.status == 'dropped_off':
                self.package_number = f"{self.dropOffLocation.tag}-{self.package_number}"
            
            if self.status == 'in_house' and self.warehouse:
                self.package_number = f"{self.warehouse.tag}-{self.package_number}"
                                
            if self.status == 'ready_for_pickup':
                self.package_number = f"{self.dropOffLocation.tag}-{self.package_number}"
                
        super().save(*args, **kwargs)

    def generate_package_number(self):
        package_number = Package.PACKAGE_PREFIX + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return package_number

    def clean(self):
        if self.dropOffLocation and self.warehouse:
            raise ValidationError("A package cannot have both drop-off location and warehouse assigned.")

    def __str__(self):
        return self.packageName
