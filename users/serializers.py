from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "full_name",
            "artistic_name",
            "password"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
    
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    


    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
           setattr(instance, key, value)

        if password is not None:
           instance.set_password(password)

        instance.save()

        return instance
