import logging
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from user.models import User

logger = logging.getLogger()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'phone_no', 'password', 'city']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.
        """
        try:
            return User.objects.create_user(**validated_data)
        except Exception as ex:
            logger.exception(ex)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)

    def create(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        if not user:
            raise serializers.ValidationError("Incorrect Credentials")
        validated_data.update({'user': user})
        self.context.update({'user': user})
        return user
