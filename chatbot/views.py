from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from util.utils import Utils, AppResponse

from rest_framework import  status
from util.utils import Utils

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout

from django.db.models import Q
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

