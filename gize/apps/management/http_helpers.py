from rest_framework.request import Request

from gize.apps.contacts.exceptions import UserNotFoundException
from gize.apps.management.auth import JWTAuthentication
from gize.apps.user.models import UserInformation


def authenticate_user(request:Request):
    authentication = JWTAuthentication
    user_id_ref = authentication.authenticate(authentication, request=request)

    try:
        return UserInformation.objects.get(user_id_ref=user_id_ref)
    except UserInformation.DoesNotExist:
        raise UserNotFoundException
