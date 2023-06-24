from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, User


# Create your models here.
class Register(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email_id = models.EmailField(max_length=30, blank=False)
    contact_no = models.CharField(max_length=100, blank=True)
    interested = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    # payment_status_choices = (
    #     (1, 'SUCCESS'),
    #     (2, 'FAILURE' ),
    #     (3, 'PENDING'),
    # )
    # payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    # razorpay_payment_id = models.CharField(max_length=500,null=True, blank=True)
    # razorpay_order_id = models.CharField(max_length=500,null=True, blank=True)
    # razorpay_signature = models.CharField(max_length=500,null=True, blank=True)
    # is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "'s Profile"