import re

from rest_framework import serializers

from gize.apps.contacts.models import Contact, PhoneType
from gize.apps.user.models import UserInformation


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def validate_user_id_ref(self, user_id):
        if user_id is None:
            raise serializers.ValidationError('User id is required.')
        
        user = UserInformation.objects.get(id=user_id)

        if not user.exists():
            raise serializers.ValidationError('User id not found.')
        
        return user
    
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
    
    def validate_status(self, status):
        if status is None or status == '':
            raise serializers.ValidationError('Status is required.')
        
        if status not in ['Ativo', 'Inativo']:
            raise serializers.ValidationError('Status must be Ativo or Inativo.')

        return status
    
    def validate_phone_type(self, phone_type):
        if phone_type is None:
            raise serializers.ValidationError('Phone type is required.')
        
        phone_type_qs = PhoneType.objects.get(slug=phone_type)

        if not phone_type_qs.exists():
            raise serializers.ValidationError('Phone type not found.')

        return phone_type_qs
    
    def validate_favorite(self, favorite):
        if favorite is None:
            raise serializers.ValidationError('Favorite is required.')
        
        if favorite not in [True, False]:
            raise serializers.ValidationError('Favorite must be True or False.')

        return favorite
    
