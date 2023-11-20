from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from gize.apps.contacts.exceptions import (AuthenticationFailed,
                                           UserNotFoundException)
from gize.apps.management.auth import JWTAuthentication
from gize.apps.management.http_helpers import authenticate_user
from gize.apps.user.models import UserInformation
from gize.apps.user.serializers import (UserInformationCreateSerializer,
                                        UserInformationSerializer)


class UserInformationViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer
    
    def list(self, request):
        user_instance = authenticate_user(request)

        serializer_instance = self.serializer_class(user_instance)

        return Response(data=serializer_instance.data, status=status.HTTP_200_OK)

    def create(self, request: Request):
        serializer = UserInformationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        UserInformation.objects.create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)
    
    def patch(self, request):
        authenticate_user(request)

        serializer = UserInformationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        UserInformation.objects.update(**serializer.validated_data)

        return Response(status=status.HTTP_200_OK)

@api_view(http_method_names=["post"])
def login_user(request: Request):
    email, password = request.data.get("email", None), request.data.get("password", None)
    
    if not email or not password:
        raise AuthenticationFailed(detail="Email or password is invalid.")

    try:
        user_instance = UserInformation.objects.get(email=email)
    except ObjectDoesNotExist:
        raise UserNotFoundException
    
    if not check_password(password=password, encoded=user_instance.password):
        raise AuthenticationFailed(detail="Email or password is invalid.")
    
    token = JWTAuthentication.create_jwt(user_instance)
    
    return Response(data={"token": token}, status=status.HTTP_200_OK)