from locust import User, between, task

# Импортируем схемы ответов, чтобы типизировать shared state
from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import OpenDepositAccountResponse
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import GetAccountsResponse

from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    1. Создаёт нового пользователя.
    2. Открывает депозит
    3. Получает список всех счетов

    Использует базовый GatewayGRPCTaskSet и уже созданных в нём API клиентов.
    """
    create_user_response: CreateUserResponse | None = None
    open_deposit_account_response: OpenDepositAccountResponse | None = None
    get_accounts_response: GetAccountsResponse | None = None

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


class GetAccountsScenarioUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий сценарий получения списка всех счетов.
    """
    tasks = [GetAccountsTaskSet]
