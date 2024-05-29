import pytest
from AuthUser.models import User, UserInfoDevices  # Замените 'myapp' на имя вашего приложения


@pytest.fixture
def user(db):
    return User.objects.create(username='testuser', password='password123')


@pytest.fixture
def device_info(user):
    return UserInfoDevices.objects.create(
        user=user,
        device='Laptop',
        browser='Chrome',
        browser_version='89.0.4389.82',
        os='Windows',
        os_version='10',
        is_bot=False
    )

@pytest.mark.django_db
def test_user_info_devices_creation(user, device_info):
    assert device_info.user == user
    assert device_info.device == 'Laptop'
    assert device_info.browser == 'Chrome'
    assert device_info.browser_version == '89.0.4389.82'
    assert device_info.os == 'Windows'
    assert device_info.os_version == '10'
    assert not device_info.is_bot

@pytest.mark.django_db
def test_user_info_devices_str_method(user, device_info):
    assert str(device_info) == 'testuser - Laptop - Chrome'
