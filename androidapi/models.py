from django.db import models

# Create your models here.
class Session(models.Model):
    sessionId = models.CharField(max_length=100,blank=True,null=True)
    datacreater = models.CharField(max_length=500,blank=True,null=True)
    datajoiner = models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.sessionId
    class Meta:
        db_table='session_table'

class BusinessDetail(models.Model):
    businessname = models.CharField(max_length=100,blank=True,null=True)
    businesstype = models.CharField(max_length=100,blank=True,null=True)
    aadhaarOwner = models.CharField(max_length=100,blank=True,null=True)
    businessaddress = models.CharField(max_length=100,blank=True,null=True)
    businessId = models.CharField(max_length=100,blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    required= models.CharField(max_length=300,blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.businessname
    class Meta:
        db_table='business_table_model'

class EKYCBusiness(models.Model):
    businessId = models.CharField(max_length=100,blank=True,null=True)
    data = models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.businessId
    class Meta:
        db_table='ekyc_table'
