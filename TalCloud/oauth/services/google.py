from rest_framework.exceptions import AuthenticationFailed
from oauth import serializers
from google.oauth2 import id_token
from google.auth.transport import requests

from oauth.models import AuthUser


def check_google_auth(google_user: serializers.GoogleAuth) -> dict:
    """Функция для приема данных от Google"""
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    # если ошибки не будет,то мы либо создаем нового пользователя, либо забираем уже существующего из БД
    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])
    return base_auth.create_token(user.id)