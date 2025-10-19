from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import IssueVirtualCardResponse, IssueVirtualCardRequest
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardRequest, IssuePhysicalCardResponse
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub


class CardsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с CardsGatewayService.
    Предоставляет высокоуровневые методы для выпуска карт.
    """
    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к CardsGatewayService.
        """
        super().__init__(channel)

        self.stub = CardsGatewayServiceStub(channel)  # gRPC-стаб, сгенерированный из .proto

    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> IssueVirtualCardResponse:
        """
        Низкоуровневый вызов метода IssueVirtualCard через gRPC.

        :param request: gRPC-запрос с ID пользователя и ID акканта пользователя
        :return: Ответ от сервиса с данными созданной виртуальной карты.
        """
        return self.stub.IssueVirtualCard(request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        """
        Низкоуровневый вызов метода IssuePhysicalCard через gRPC.

        :param request: gRPC-запрос с ID пользователя и ID акканта пользователя
        :return: Ответ от сервиса с данными созданной физической карты.
        """
        return self.stub.IssuePhysicalCard(request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponse:
        """
        метод выпуска виртуальной карты

        :param user_id: ID пользователя
        :param account_id: ID аккаунта пользователя
        :return: Ответ от сервиса с данными созданной виртуальной карты.
        """
        request = IssueVirtualCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_virtual_card_api(request)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        """
        метод выпуска физической карты

        :param user_id: ID пользователя
        :param account_id: ID аккаунта пользователя
        :return: Ответ от сервиса с данными созданной физической карты.
        """
        request = IssuePhysicalCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_physical_card_api(request)


def build_cards_gateway_grpc_client() -> CardsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра CardsGatewayGRPCClient.

    :return: Инициализированный клиент для CardsGatewayService.
    """
    return CardsGatewayGRPCClient(channel=build_gateway_grpc_client())

def build_cards_gateway_locust_grpc_client(environment: Environment) -> CardsGatewayGRPCClient:
    """
    Функция создаёт экземпляр CardsGatewayGRPCClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр CardsGatewayGRPCClient с хуками сбора метрик.
    """
    return CardsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))