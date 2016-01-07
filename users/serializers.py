from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'],
                                        first_name=validated_data.get('first_name'),
                                        last_name=validated_data.get('last_name')
                                        )

        return user

