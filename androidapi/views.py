from django.shortcuts import render
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,JsonResponse
import json
from .models import *
from datetime import datetime
from datetime import *
# Create your views here.

class createSession(APIView):
    def post(self,request):
        datasender = request.POST.get('data')
        session = Session()
        myid = datetime.now().strftime('%d%m%Y%H%M%S')
        session.sessionId = str(myid)
        session.datacreater = datasender
        session.save()
        return HttpResponse(session.sessionId)
class joinSession(APIView):
    def post(self,request):
        datajoiner = request.POST.get('data')
        sessionid = request.POST.get('id')
        try:
            session = Session.objects.get(sessionId = sessionid)
            session.datajoiner = datajoiner
            session.save()
            return HttpResponse(session.datacreater)
        except ObjectDoesNotExist:
            return HttpResponse('failed')

class businessRegister(APIView):
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        type = request.POST.get('type')
        aadhaar = request.POST.get('aadhaar')
        address = request.POST.get('address')
        password = request.POST.get('password')
        required = request.POST.get('required')
        try:
            detail = BusinessDetail()
            detail.businessId = email
            detail.businessname = name
            detail.businesstype = type
            detail.aadhaarOwner = aadhaar
            detail.businessaddress = address
            detail.password = password
            detail.required = required
            detail.save()
            return HttpResponse("data saved")
        except Exception as e:
            return HttpResponse("Error")
class businessLogin(APIView):
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            detail = BusinessDetail.objects.get(businessId = email,password = password)
            return HttpResponse('login successfull')
        except ObjectDoesNotExist:
            return HttpResponse('login failed')

class getBusinessNames(APIView):
    def post(self,request):
        try:
            detail = BusinessDetail.objects.all()
            ar=[]
            for value in detail:
                dict={}
                dict['name'] = value.businessname
                dict['id'] = value.businessId
                ar.append(dict)
            return HttpResponse(json.dumps(ar))
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(ar))

class fillEKYC(APIView):
    def post(self,request):
        id = request.POST.get('id')
        data = request.POST.get('data')
        try:
            ekyc = EKYCBusiness()
            ekyc.businessId = id
            ekyc.data = data
            ekyc.save()
            return HttpResponse('data saved')
        except ObjectDoesNotExist:
            return HttpResponse('Error')

class seeEKYC(APIView):
    def post(self,request):
        id = request.POST.get('id')
        ar=[]
        try:
            ekyc = EKYCBusiness.objects.filter(businessId=id)
            for value in ekyc:
                dict={}
                dict['data']=value.data
                ar.append(dict)
            return HttpResponse(json.dumps(ar))
        except ObjectDoesNotExist:
            return HttpResponse('DoesNotExist')
