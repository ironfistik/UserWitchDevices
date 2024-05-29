from rest_framework import serializers
from .models import User, UserInfoDevices


class UserInfoDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoDevices
        fields = "__all__"
        read_only_fields = ('user', 'created_at')


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания пользователя"""

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        """Функция для хэширования пароля"""
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления пользователя"""

    class Meta:
        model = User
        fields = "__all__"


class UserDestroySerializer(serializers.ModelSerializer):
    """Сериализатор для удаления пользователя"""

    class Meta:
        model = User
        fields = ["id"]
