from django.db import models

# Create your models here.
class Vendor(models.Model):
    auth_token = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    BUSINESS_TYPE = (
        (u'yarn', u'yarn'),
        (u'fabric', u'fabric'),
        (u'garment', u'garment'),
        (u'home', u'home'),
        (u'others', u'others'),
    )
    business_type = models.CharField(max_length=15, choices=BUSINESS_TYPE, blank=False)

    kind_of_products = models.CharField(max_length=1000, blank=True)
    company_website = models.CharField(max_length=100, blank=True)
    company_address = models.CharField(max_length=500, blank=True)
    information = models.CharField(max_length=1000, blank=True)
    name_of_person = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(max_length=100, blank=False)
    contact_phone = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name + "'s Profile"


class General_Listing(models.Model):
    auth_token = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    company_address = models.CharField(max_length=500, blank=True)
    contact_email = models.EmailField(max_length=100, blank=False)
    contact_phone = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name 


class Empaneled_Vendor(models.Model):
    auth_token = models.CharField(max_length=100, blank=True)
    user_image = models.ImageField(upload_to="Empaneled_Vendor" ,blank=True)
    company_profile = models.ImageField(upload_to="Empaneled_Vendor" ,blank=True)
    small_video = models.ImageField(upload_to="Empaneled_Vendor" ,blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    BUSINESS_TYPE = (
        (u'yarn', u'yarn'),
        (u'fabric', u'fabric'),
        (u'garment', u'garment'),
        (u'home', u'home'),
        (u'others', u'others'),
    )
    business_type = models.CharField(max_length=15, choices=BUSINESS_TYPE, blank=False)

    kind_of_products = models.CharField(max_length=1000, blank=True)
    company_website = models.CharField(max_length=100, blank=True)
    company_address = models.CharField(max_length=500, blank=True)
    information = models.CharField(max_length=1000, blank=True)
    name_of_person = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(max_length=100, blank=False)
    contact_phone = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name 