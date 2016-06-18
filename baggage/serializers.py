from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    # email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        t_username = validated_data['username']
        t_password = validated_data['password']
        t_email = validated_data['username'] + '@test.com'
        return User.objects.create_user(
            username=t_username,
            email=t_email,
            password=t_password,
        )

    def update(self, instance, validated_data):
        return None

