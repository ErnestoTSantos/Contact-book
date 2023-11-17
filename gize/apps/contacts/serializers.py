import re

from rest_framework import serializers

from gize.apps.contacts.models import Contact, PhoneType


class PhoneTypeSerializer(serializers.Serializer):
    phone_type = serializers.CharField()

    def validate_phone_type(self, phone_type):
        if phone_type is None:
            raise serializers.ValidationError('Phone type is required.')
        
        phone_type_instance = PhoneType.objects.get(name=phone_type) or None

        if not phone_type_instance:
            raise serializers.ValidationError('Phone type not found.')

        return phone_type_instance.id


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    phone_type = PhoneTypeSerializer(required=True, )
    
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

        return phone
    
    def validate_favorite(self, favorite):
        if favorite is None:
            raise serializers.ValidationError('Favorite is required.')

        return favorite
    
