from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Структура данных для операций
    """
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Структура данных для рецепта
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Структура данных для получения списка операций пользователя
    """
    spentAmount: int
    receivedAmount: int
    cashbackAmount: int


class GetOperationQueryDict(TypedDict):
    """
    Структура данных для получения списка операций пользователя
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для отправления запроса на платёжные операции
    """
    status: str
    amount: int
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для отправления запроса на операцию покупки
    """
    status: str
    amount: int
    cardId: str
    accountId: str
    category: str


class GetOperationsResponseDict(TypedDict):
    """
    Структура данных для ответа получения операций
    """
    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура данных для ответа сводки по операциям
    """
    operations: OperationsSummaryDict


class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура данных для ответа по операции
    """
    receipt: OperationReceiptDict


class GetOperationResponseDict(TypedDict):
    """
    Структура данных для ответа по получению операции
    """
    operation: OperationDict


class MakeFeeResponseDict(TypedDict):
    """
    Структура данных для ответа по операции налога
    """
    response: MakeOperationRequestDict


class MakeTopUpResponseDict(TypedDict):
    """
    Структура данных для ответа по операции создания карты
    """
    response: MakeOperationRequestDict


class MakeCashBackResponseDict(TypedDict):
    """
    Структура данных для ответа по операции кэшбек
    """
    response: MakeOperationRequestDict


class MakeTransferResponseDict(TypedDict):
    """
    Структура данных для ответа по операции перевода
    """
    response: MakeOperationRequestDict


class MakePurchaseResponseDict(TypedDict):
    """
    Структура данных для ответа по операции покупки
    """
    response: MakePurchaseOperationRequestDict


class MakeBillResponseDict(TypedDict):
    """
    Структура данных для ответа по операции счёта
    """
    response: MakeOperationRequestDict


class MakeCashResponseDict(TypedDict):
    """
    Структура данных для ответа по операции снятия
    """
    response: MakeOperationRequestDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по operation_id

        :param operation_id: Строка с operation_id, например '123'.
        :return: Объект httpx.Response с данными об операции с operation_id
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id

        :param operation_id: Строка с operation_id, например '123'.
        :return: Объект httpx.Response с данными о чеке по операции с operation_id
        """
        return self.get(f"/api/v1/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определённого счёта

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными списка операций для определённого счёта
        """
        return self.get("/api/v1/operations/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определённого счёта

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции комиссии

        :param request: Словарь с параметрами запроса, например: {
                                                                  "status": "FAILED",
                                                                  "amount": 0,
                                                                  "cardId": "string",
                                                                  "accountId": "string"
                                                                }.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции пополнения

        :param request: Словарь с параметрами запроса, например: {
                                                                  "status": "FAILED",
                                                                  "amount": 0,
                                                                  "cardId": "string",
                                                                  "accountId": "string"
                                                                }.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции кэшбэка

        :param request: Словарь с параметрами запроса, например: {
                                                                  "status": "FAILED",
                                                                  "amount": 0,
                                                                  "cardId": "string",
                                                                  "accountId": "string"
                                                                }.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции перевода

        :param request: Словарь с параметрами запроса, например: {
                                                                  "status": "FAILED",
                                                                  "amount": 0,
                                                                  "cardId": "string",
                                                                  "accountId": "string"
                                                                }.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции покупки

        :param request: Словарь с параметрами запроса, например: {
                                                                  "status": "FAILED",
                                                                  "amount": 0,
                                                                  "cardId": "string",
                                                                  "accountId": "string",
                                                                  "category": "string"
                                                                }
        :return: Объект httpx.Response с данными об операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции оплаты по счету

        :param request: Словарь с параметрами запроса, например: {
                                                                  "status": "FAILED",
                                                                  "amount": 0,
                                                                  "cardId": "string",
                                                                  "accountId": "string"
                                                                }.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции снятия наличных денег

        :param request: Словарь с параметрами запроса, например: {
                                                                  "status": "FAILED",
                                                                  "amount": 0,
                                                                  "cardId": "string",
                                                                  "accountId": "string"
                                                                }.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Вызов метода get_operation_api

        :param operation_id: Строка с operation_id, например '123'.
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Вызов метода get_operation_receipt

        :param operation_id: Строка с operation_id, например '123'.
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, query: GetOperationQueryDict) -> GetOperationsResponseDict:
        """
        Вызов метода get_operations

        :param query: Словарь типа GetOperationQueryDict
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, query: GetOperationQueryDict) -> GetOperationsSummaryResponseDict:
        """
        Вызов метода get_operations_summary

        :param query: Словарь типа GetOperationQueryDict
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeResponseDict:
        """
        Вызов метода make_fee_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestDict(
            status='COMPLETED',
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpResponseDict:
        """
        Вызов метода make_top_up_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestDict(
            status='COMPLETED',
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashBackResponseDict:
        """
        Вызов метода make_cashback_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestDict(
            status='COMPLETED',
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferResponseDict:
        """
        Вызов метода make_transfer_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestDict(
            status='COMPLETED',
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str, category: str) -> MakePurchaseResponseDict:
        """
        Вызов метода make_purchase_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :param category: строка, категория
        :return: Ответ от сервера (объект JSON).
        """
        request = MakePurchaseOperationRequestDict(
            status='COMPLETED',
            amount=1000,
            cardId=card_id,
            accountId=account_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillResponseDict:
        """
        Вызов метода make_bill_payment_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestDict(
            status='COMPLETED',
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashResponseDict:
        """
        Вызов метода make_cash_withdrawal_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestDict(
            status='COMPLETED',
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
