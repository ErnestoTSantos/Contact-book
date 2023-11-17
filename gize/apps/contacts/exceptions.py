from rest_framework import status
from rest_framework.exceptions import APIException


class UserNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User informations not found"
    default_code = "UserInformationsNotFound"

class AuthenticationFailed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "Authentication failed"
    default_detail = "Email or password incorrect"