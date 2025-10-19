from locust import User, between, task

from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.schema import OpenDepositAccountResponseSchema
from clients.http.gateway.accounts.schema import GetAccountsResponseSchema

from clients.http.gateway.locust import GatewayHTTPTaskSet


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    """
    1. Создаёт нового пользователя.
    2. Открывает депозит
    3. Получает список всех счетов

    Использует базовый GatewayHTTPTaskSet и уже созданных в нём API клиентов.
    """
    create_user_response: CreateUserResponseSchema | None = None
    open_deposit_account_response: OpenDepositAccountResponseSchema | None = None
    get_accounts_response: GetAccountsResponseSchema | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()


    @task(2)
    def open_deposit_account(self):
        """
        Открытие счета, если создан пользователь
        """
        if not self.create_user_response:
            return
        self.open_deposit_account_response = self.accounts_gateway_client.open_deposit_account(
            self.create_user_response.user.id
        )

    @task(6)
    def get_accounts(self):
        """
        Получение списка всех счетов, если создан пользователь и у него есть хотя бы один счёт
        """
        if not self.create_user_response and not self.open_deposit_account_response:
            return
        self.get_accounts_response = self.accounts_gateway_client.get_accounts(
            self.create_user_response.user.id
        )


class GetAccountsScenarioUser(User):
    """
    Пользователь Locust, исполняющий сценарий получения списка всех счетов.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)
