from django.urls import path
from AuthUser.views import UserCreateView, UserUpdateView, UserDeleteView, UserLogin

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('login/', UserLogin.as_view(), name='login_user_devices'),
]