from rest_framework import serializers

from .models import Portfolio, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("full_name", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PortfolioSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Portfolio
        fields = ("id", "user", "title")
