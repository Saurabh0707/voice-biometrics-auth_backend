from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'voiceit_id', 'password')

        extra_kwargs = {'password':{ 'write_only' : True}}

    def create(self, validated_data):
        user = models.UserProfile(
            email = validated_data['email'],
            voiceit_id  = validated_data['voiceit_id']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user