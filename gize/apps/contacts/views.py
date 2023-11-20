from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from gize.apps.contacts.exceptions import ContactExists, ContactNotExists
from gize.apps.contacts.models import Contact, PhoneType
from gize.apps.contacts.serializers import (ContactSerializers,
                                            PhoneTypeSerializer)
from gize.apps.management.http_helpers import authenticate_user


class PhoneTypeView(ListAPIView):
    queryset = PhoneType.objects.all()
    serializer_class = PhoneTypeSerializer

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

        contact_exists = Contact.objects.filter(user_id_ref=user_instance.user_id_ref, phone=request.data.get("phone"))

        if contact_exists.exists():
            raise ContactExists
        
        return Response(status=status.HTTP_201_CREATED)
    

    def partial_update(self, request, pk=None):
        user_instance = authenticate_user(request)

        contact_instance = Contact.objects.filter(user_id_ref=user_instance.user_id_ref, id=pk)

        if not contact_instance.exists():
            raise ContactNotExists

        serializer = ContactSerializers(instance=contact_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        contact_instance.update(**serializer.validated_data)
        
        return Response(status=status.HTTP_200_OK) 

    def retrieve(self, request, pk=None):
        user_instance = authenticate_user(request)

        try:
            contact_instance = Contact.objects.get(user_id_ref=user_instance.user_id_ref, id=pk)
        except Contact.DoesNotExist:
            raise ContactNotExists

        serializer = ContactSerializers(instance=contact_instance)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_instance = authenticate_user(request)

        contact_instance = Contact.objects.filter(user_id_ref=user_instance.user_id_ref, id=pk)

        if not contact_instance.exists():
            raise ContactNotExists
        
        contact_instance.get().delete()
        
        return Response(status=status.HTTP_200_OK)
        
