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

class ContactExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Existing contact for this user."
    default_code = "User contact exists"

class ContactNotExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Not found this contact for user."
    default_code = "User contact not found"