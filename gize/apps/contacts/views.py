from rest_framework import status, viewsets
from rest_framework.response import Response

from gize.apps.contacts.exceptions import UserNotFoundException
from gize.apps.contacts.models import Contact
from gize.apps.contacts.serializers import ContactSerializers
from gize.apps.management.http_helpers import authenticate_user


class ContactViewSet(viewsets.ViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

    def list(self, request):
        user_instance = authenticate_user(request)

        qs = Contact.objects.filter(user_id_ref=user_instance.user_id_ref)

        serializer_instance = self.serializer_class(qs, many=True)

        return Response(data=serializer_instance.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_instance = authenticate_user(request)

        serializer = ContactSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        Contact.objects.create(user_id_ref=user_instance.user_id_ref, **serializer.validated_data)

        return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass