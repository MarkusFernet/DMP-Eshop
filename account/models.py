import uuid
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.html import strip_tags


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):

        if not email:
            raise ValueError(('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def email_user(self, subject, message, html_message):
        # Set up the email headers
        from_email = 'markusfernet@gmail.com'
        recipient_list = [self.email]

        # Send the email using the send_mail function
        send_mail(
            subject,
            strip_tags(message),  # Plain text version of the email message
            from_email,
            recipient_list,
            html_message=html_message,  # HTML version of the email message
            fail_silently=False,
        )

    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, verbose_name=("Customer"), on_delete=models.CASCADE)
    full_name = models.CharField(("Full Name"), max_length=150)
    phone = models.CharField(("Phone Number"), max_length=50)
    postcode = models.CharField(("Postcode"), max_length=50)
    address_line = models.CharField(("Address Line 1"), max_length=255)
    address_line2 = models.CharField(("Address Line 2"), max_length=255)
    town_city = models.CharField(("Town/City/State"), max_length=150)
    delivery_instructions = models.CharField(("Delivery Instructions"), max_length=255)
    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)
    default = models.BooleanField(("Default"), default=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "Address"
