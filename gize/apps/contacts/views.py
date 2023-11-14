from rest_framework import viewsets

from gize.apps.contacts.models import Contact
from gize.apps.contacts.serializers import ContactSerializers


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
