from django.contrib.auth.models import Group
from backendApp.models import User, Client
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class ClientSerializer(serializers.ModelSerializer):  
    user = UserSerializer(required=True)

    class Meta:
        model = Client
        fields = ('user', 'voiceitId',)

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        client= Client.objects.create(user=user, voiceitId=validated_data.pop('voiceitId'))
        return client
    
    def update(self, instance, validated_data):
        instance.voiceitId = validated_data.get('voiceitId', instance.voiceitId)
        # instance.save()
        return instance