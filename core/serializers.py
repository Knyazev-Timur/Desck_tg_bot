from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed, NotAuthenticated

USER_MODEL = get_user_model()

class PassswordField(serializers.Charfield):

    def __init__(self, **kwargs):
        kwargs['style'] = {'input_type': 'password'}
        kwargs.setdefault('write_only', True)
        super.__init__(**kwargs)
        self.validators.append(validate_password)


class RegistrationSerilazer(serializers.ModelSerializer):
    password = PassswordField(required=True)
    password_repeat = PassswordField(required=True)

    class Meta:
        model = USER_MODEL
        read_only_fields = ('id',)
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'password_repeat',
        )

    def validate(self, attrs: dict):
        if attrs['password'] != attrs['password_repeat']:
            raise ValidationError('password is not confirmed')
        return attrs

    def create(self, validated_data: dict) -> USER_MODEL:
        del validated_data['password_repeat']
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)




