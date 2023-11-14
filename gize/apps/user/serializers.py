from rest_framework import serializers

from gize.apps.user.models import UserInformation


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = '__all__'