from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient


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
