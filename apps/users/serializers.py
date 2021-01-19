from django.contrib.auth.models import User, Group
from django.core import exceptions
from django.contrib.auth import password_validation as validators
from django.http import request

from rest_framework.fields import EmailField
from rest_framework.validators import UniqueValidator
from rest_framework.serializers import ModelSerializer


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class UserSerializer(ModelSerializer):
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('__all__')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        current_user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            current_user = request.user
        if (not current_user.is_authenticated 
            or not getattr(current_user, 'is_superuser', False)):
            self.validated_data.pop('is_superuser')
            self.validated_data.pop('is_staff')
        return super(UserSerializer, self).save(**kwargs)

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            **validated_data
        )
        return user

    def validate(self, data):
        if self.instance is None:
            user = User(**data)
            password = data.get('password')
            errors = dict()
            try:
                validators.validate_password(password=password, user=user)

            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)

            if errors:
                raise exceptions.ValidationError(errors)
        return super(UserSerializer, self).validate(data)