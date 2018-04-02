from django.db import models

# Create your models here.
class Session(models.Model):
    sessionId = models.CharField(max_length=100)
    datacreater = models.CharField(max_length=500)
    datajoiner = models.CharField(max_length=500)
    def __str__(self):              # __unicode__ on Python 2
        return self.sessionId
    class Meta:
        db_table='session_table'

class BusinessDetail(models.Model):
    businessname = models.CharField(max_length=100)
    businesstype = models.CharField(max_length=100)
    aadhaarOwner = models.CharField(max_length=100)
    businessaddress = models.CharField(max_length=100)
    businessId = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    required= models.CharField(max_length=300)
    def __str__(self):              # __unicode__ on Python 2
        return self.businessname
    class Meta:
        db_table='business_table_model'

class EKYCBusiness(models.Model):
    businessId = models.CharField(max_length=100)
    data = models.CharField(max_length=500)
    def __str__(self):              # __unicode__ on Python 2
        return self.businessId
    class Meta:
        db_table='ekyc_table'
