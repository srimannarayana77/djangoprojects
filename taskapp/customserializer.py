# serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()

            if user and user.check_password(password):
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError('Incorrect email or password.')
        else:
            raise serializers.ValidationError('Email and password must be provided.')
