from django_user_agents.utils import get_user_agent
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from AuthUser.models import User, UserInfoDevices
from AuthUser.serializers import UserCreateSerializer, UserUpdateSerializer, UserDestroySerializer, \
    UserInfoDevicesSerializer


class UserLogin(ObtainAuthToken):
    """Класс для авторизации и получения мнформации о девайсе"""

    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)
        device = "unknown"
        if user_agent.is_mobile:
            device = "mobile"
        elif user_agent.is_tablet:
            device = "tablet"
        elif user_agent.is_pc:
            device = "PC"

        user_device_info = UserInfoDevices.objects.create(
            user=request.user,
            device=device,
            browser=user_agent.browser.family,
            browser_version=user_agent.browser.version_string,
            os=user_agent.os.family,
            os_version=user_agent.os.version_string,
            is_bot=user_agent.is_bot
        )

        serializer = UserInfoDevicesSerializer(user_device_info)
        return Response(serializer.data)


class UserCreateView(CreateAPIView):
    """Класс для создания пользователя"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    """Класс для обновления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    # permission_classes = [IsAuthenticated]


class UserDeleteView(DestroyAPIView):
    """Класс для удаления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
    # permission_classes = [IsAuthenticated]
