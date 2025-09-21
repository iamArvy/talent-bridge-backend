from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "email", "password", "role"]
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}

    def validate_password(self, value):
        user = User(email=self.initial_data.get("email"))
        validate_password(value, user)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            role=validated_data.get("role", "applicant"),
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print(user)
        token = super().get_token(user)
        token["email"] = user.email
        token["role"] = user.role
        return token
