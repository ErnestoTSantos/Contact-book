import json
import re

from rest_framework import serializers

from gize.apps.contacts.models import Contact, PhoneType


class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneType
        fields = ('id', 'name',)


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    phone_type = serializers.CharField(required=True)
    favorite = serializers.BooleanField(required=False)
    
    def validate_name(self, name):
        if name is None or name == '':
            raise serializers.ValidationError('Name is required.')
        
        if len(name) < 3:
            raise serializers.ValidationError('Name must be at least 3 characters.')

        return name
    
    def validate_phone(self, phone):
        if phone is None or phone == '':
            raise serializers.ValidationError('Phone is required.')
        
        if re.sub(r"[^0-9+() -]", "", phone) != phone:
            raise serializers.ValidationError('Phone must be a valid number.')
        
        if len(phone) != 11:
            raise serializers.ValidationError('Phone needs just 11 chars. Ex: dd + 999999999')

        return phone
        
    def validate_phone_type(self, phone_type):
        try:
            return PhoneType.objects.get(name=phone_type)
        except PhoneType.DoesNotExist:
            raise serializers.ValidationError('Phone type not found.')
    
