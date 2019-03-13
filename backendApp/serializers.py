from django.contrib.auth.models import Group
from backendApp.models import User, Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Client
        fields = ('voiceitId',)

    # def create(self, validated_data):
    #     """
    #     Overriding the default create method of the Model serializer.
    #     :param validated_data: data containing all the details of student
    #     :return: returns a successfully created student record
    #     """
    #     user_data = validated_data.pop('user')
    #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
    #     client= Client.objects.create(user=user, voiceitId=validated_data.pop('voiceitId'))
    #     return client
    
    # def update(self, instance, validated_data):
    #     instance.voiceitId = validated_data.get('voiceitId', instance.voiceitId)
    #     # instance.save()
    #     return instance


class UserSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'client')
    
    def create(self, validated_data):
        clients_data = validated_data.pop('client').pop('voiceitId')
        user = User.objects.create(**validated_data)
        # for client_data in clients_data:
        Client.objects.create(user=user, voiceitId= clients_data)
        return user
    # def update(self, instance, validated_data):
    #     instance.voiceitId = validated_data.get('voiceitId', instance.voiceitId)
    #     # instance.save()
    #     return instance