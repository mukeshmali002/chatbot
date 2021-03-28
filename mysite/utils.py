from rest_framework.views import exception_handler
from util.utils import Utils, AppResponse
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    exe_response = exception_handler(exc, context)
    if exe_response is not None :    
        response = AppResponse.responseMsg(
                    request=None, 
                    status=False, 
                    status_code=exe_response.status_code, 
                    message=exe_response.data.get('detail'),
                    result={}) 
        return Response(response,status=exe_response.status_code)