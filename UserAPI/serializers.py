from rest_framework import serializers
from UserAPI.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('displayName','email','phoneNumber','photoURL','uid')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','points')
        depth=1
