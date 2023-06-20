from rest_framework import serializers
from django.db.models import fields
from django.contrib.auth import get_user_model

User = get_user_model

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'birthYMD')

class ChangePasswordSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password')
        read_only_fields = ('email', 'birthYMD')