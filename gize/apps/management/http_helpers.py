from rest_framework.request import Request

from gize.apps.management.auth import JWTAuthentication
from gize.apps.user.models import UserInformation


def authenticate_user(request:Request):
    authentication = JWTAuthentication
    user_id_ref = authentication.authenticate(authentication, request=request)

    user_instance = UserInformation.objects.get(user_id_ref=user_id_ref)

    return user_instance