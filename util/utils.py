import json
import base64 
import os

from datetime import date, datetime
from django.utils import timezone
from django.core.cache import cache
from decimal import *
from uuid import uuid4
from django.conf import settings

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework import status

from django.contrib.auth.models import User
import base64, hashlib, codecs

class AppResponse(object):

    @staticmethod
    def responseSuccess(request, message):
        return { 
            "status" : True,
            "status_code" : status.HTTP_200_OK,
            "message" : message, 
            "recordsTotal" : 0,
            "result" : {} ,
        }

    @staticmethod
    def responseMsg(request, status, status_code, message, result={}):
        return { 
            "status" : status,
            "status_code" : status_code,
            "message" : message, 
            "recordsTotal" : 0,
            "result" : {} ,
        }
    
    @staticmethod
    def responseMsg404(request, message):
        return { 
            "status" : False,
            "status_code" : status.HTTP_404_NOT_FOUND,
            "message" : message, 
            "recordsTotal" : 0,
            "result" : {} ,
        }

    @staticmethod
    def responseMsg401(request, message):
        return { 
            "status" : False,
            "status_code" : status.HTTP_404_NOT_FOUND,
            "message" : message, 
            "recordsTotal" : 0,
            "result" : {} ,
        }

    @staticmethod
    def responseList(request, message='', recordsTotal=0, result={}):       
        return { 
            "status" : True,
            "status_code" : status.HTTP_200_OK,
            "message" : message, 
            "recordsTotal" : recordsTotal,
            "result" : result ,
        }

class Utils(object):

    @staticmethod    
    def isNumber(data):
        try:
            int(data)
            return True
        except ValueError:
            return False

    @staticmethod    
    def datetimeNow():
        return datetime.datetime.now()

    @staticmethod    
    def getBrowserAgent(request) :
        return request.META.get('HTTP_USER_AGENT','') 

    @staticmethod    
    def getClientIp(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        else:
            return request.META.get('REMOTE_ADDR')


