from locust import User, between, task

from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema


class OpenDebitCardAccountScenarioUser(User):
    """
    Класс для создания сценариев по открытию счёта
    """
    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient

    create_user_response: CreateUserResponseSchema
    open_debit_card_response: OpenDebitCardAccountResponseSchema

    def on_start(self):
        """
        Создание пользователя
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)

        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        """
        Открытие счёта
        """
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)

        self.open_debit_card_response = self.accounts_gateway_client.open_debit_card_account(
            self.create_user_response.user.id)
