import re

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from gize.apps.user.models import UserInformation


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ['id', 'name', 'email', 'birthday']

class UserInformationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = "__all__"

    def validate_email(self, email):
        if not email:
            raise serializers.ValidationError("This field cannot be empty.")
        
        if UserInformation.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already used.")
        
        if re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]$', email):
            raise serializers.ValidationError("Incorrect format e-mail.")
        
        return email
        

    def validate_password(self, password):
        if not password:
            raise serializers.ValidationError("This field cannot be empty.")
        
        if " " in password:
            raise serializers.ValidationError("Password cannot have space.")
        
        # define our regex pattern for validation
        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"

        # We use the re.match function to test the password against the pattern
        match = re.match(pattern, password)

        if bool(match):
            raise serializers.ValidationError("Password needs more be stronger.")

        return make_password(password)
