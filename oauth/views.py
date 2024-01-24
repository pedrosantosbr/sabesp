from django.utils.module_loading import import_string
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.conf import settings

# from .authentication import AUTH_HEADER_TYPES
# from .exceptions import InvalidToken, TokenError
# from .settings import api_settings

from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from types import Dict, Any
from django.contrib.auth.models import update_last_login


class TokenOauth2Serializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class TokenViewBase(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = None
    _serializer_class = ""

    www_authenticate_realm = "api"

    def get_serializer_class(self) -> Serializer:
        """
        If serializer_class is set, use it directly. Otherwise get the class from settings.
        """

        if self.serializer_class:
            return self.serializer_class
        try:
            return import_string(self._serializer_class)
        except ImportError:
            msg = "Could not import serializer '%s'" % self._serializer_class
            raise ImportError(msg)

    def get_authenticate_header(self, request: Request) -> str:
        return '{} realm="{}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def post(self, request: Request, *args, **kwargs) -> Response:
        print(request.data)
        client_id = request.data.get("client_id", None)
        client_secret = request.data.get("client_secret", None)

        if client_id is None or client_secret is None:
            return Response(
                {"detail": "Client credentials not provided"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        authorized_clients = {settings.SABESP_CLIENT_ID: settings.SABESP_CLIENT_SECRET}

        if client_id in authorized_clients:
            if client_secret == authorized_clients[client_id]:
                serializer = self.get_serializer(data=request.data)
                try:
                    serializer.is_valid(raise_exception=True)
                except TokenError as e:
                    raise InvalidToken(e.args[0])

                return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Client credentials not valid"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class TokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER


token_obtain_pair = TokenObtainPairView.as_view()
