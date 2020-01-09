import json

from meiga import Success, Failure, Result

from .auth_client import AuthClient
from alice.config import Config
from .auth_errors import AuthError

DEFAULT_URL = "https://apis.alicebiometrics.com/auth"


class Auth:
    @staticmethod
    def from_config(config: Config):
        return Auth(api_key=config.api_key, base_url=config.auth_url)

    def __init__(
        self, api_key, service_id: str = "onboarding", base_url: str = DEFAULT_URL
    ):
        self._auth_client = AuthClient(base_url, api_key)
        self._service_id = service_id

    def create_backend_token(self, user_id: str = None) -> Result[str, AuthError]:
        """
        Returns a BACKEND_TOKEN or BACKEND_TOKEN_WITH_USER depending of user_id given parameter.
        Both BACKEND_TOKEN and BACKEND_TOKEN_WITH_USER are used to secure global requests.

        Parameters
        ----------
        user_id
            User identifier


        Returns
        -------
            A Result where if the operation is successful it returns BACKEND_TOKEN or BACKEND_TOKEN_WITH_USER.
            Otherwise, it returns an OnboardingError.
        """
        response = self._auth_client.create_backend_token(self._service_id, user_id)

        if response.status_code == 200:
            return Success(self.__get_token_from_response(response))
        else:
            return Failure(
                AuthError.from_response(
                    operation="create_backend_token", response=response
                )
            )

    def create_user_token(self, user_id: str) -> Result[str, AuthError]:
        """
        Returns a USER_TOKEN.
        The USER_TOKEN is used to secure requests made by the users on their mobile devices or web clients.


        Parameters
        ----------
        user_id
            User identifier


        Returns
        -------
            A Result where if the operation is successful it returns USER_TOKEN.
            Otherwise, it returns an OnboardingError.
        """
        response = self._auth_client.create_user_token(self._service_id, user_id)

        if response.status_code == 200:
            return Success(self.__get_token_from_response(response))
        else:
            return Failure(
                AuthError.from_response(
                    operation="create_user_token", response=response
                )
            )

    @staticmethod
    def __get_token_from_response(response):
        response_json = json.loads(response.content)
        token = response_json["token"]
        return token