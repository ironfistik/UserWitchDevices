from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # подключение api для авторизации из DRF
    path('user/', include('AuthUser.urls')),
]
