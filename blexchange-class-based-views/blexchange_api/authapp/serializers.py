from django.dispatch import receiver
from requests import request
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Link, CustomUser, activity



class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email','password', 'password2',)
        extra_kwargs = {
            'username': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
        
    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email = validated_data['email'],
        )

        return user



class AddLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link

        # fields = (
        #     'owner', 'link', 'niche', 'title'
        # )

        fields = '__all__'
        extra_kwargs = {
            'title': {
                'required': True, 'allow_blank': False,
            },
            'niche': {
                'required': True, 'allow_blank': False,
            },
            'link': {
                'required': True, 'allow_blank': False,
                'validators': [UniqueValidator(Link.objects.all(), 'Link has been posted already'),]
            }
        }

    def create(self, validated_data):
        new_link = Link.objects.create(
            title = validated_data.get('title'),
            niche = validated_data.get('niche'), 
            link = validated_data.get('link'),
            owner = validated_data.get('owner')
        )

        return new_link


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = activity

        # fields = (
        #     'owner', 'link', 'niche', 'title'
        # )

        fields = '__all__'
        valid = {
            'allow_blank': False, 'required': True,
        }
        extra_kwargs = {
            'status': valid, 'type': valid
        }

    def create(self, validated_data):
        new_activity = Link.objects.create(
            sender = validated_data.get('sender'),
            receiver = validated_data.get('receiver'),
            sender_link = validated_data.get('sender_link'),
            receiver_link = validated_data.get('receiver_link'),
            status = validated_data.get('status'),
            type = validated_data.get('type'),
            
        )

        return new_activity

