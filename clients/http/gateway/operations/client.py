from httpx import Response, QueryParams
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import (
    build_gateway_http_client,
    build_gateway_locust_http_client
)
from clients.http.gateway.operations.schema import (
    GetOperationQuerySchema,
    GetOperationsResponseSchema,
    GetOperationResponseSchema,
    GetOperationsSummaryResponseSchema,
    GetOperationReceiptResponseSchema,
    MakeFeeResponseSchema,
    MakeBillResponseSchema,
    MakeCashResponseSchema,
    MakeOperationRequestSchema,
    MakePurchaseResponseSchema,
    MakeTransferResponseSchema,
    MakeTopUpResponseSchema,
    MakeCashBackResponseSchema,
    MakePurchaseOperationRequestSchema)

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
        return self.get(f"/api/v1/operations/{operation_id}",
                        extensions=HTTPClientExtensions(route="/api/v1/operations/{operation_id}"))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id

        :param operation_id: Строка с operation_id, например '123'.
        :return: Объект httpx.Response с данными о чеке по операции с operation_id
        """
        return self.get(f"/api/v1/operation-receipt/{operation_id}",
                        extensions=HTTPClientExtensions(route="/api/v1/operations/operation-receipt/{operation_id}"))

    def get_operations_api(self, query: GetOperationQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определённого счёта

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными списка операций для определённого счёта
        """
        return self.get("/api/v1/operations/operations", params=QueryParams(**query.model_dump(by_alias=True)),
                        extensions=HTTPClientExtensions(route="/api/v1/operations"))

    def get_operations_summary_api(self, query: GetOperationQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определённого счёта

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)),
                        extensions=HTTPClientExtensions(route="/api/v1/operations/operations-summary"))

    def make_fee_operation_api(self, request: MakeOperationRequestSchema) -> Response:
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
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeOperationRequestSchema) -> Response:
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
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeOperationRequestSchema) -> Response:
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
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeOperationRequestSchema) -> Response:
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
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
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
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeOperationRequestSchema) -> Response:
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
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestSchema) -> Response:
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
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Вызов метода get_operation_api

        :param operation_id: Строка с operation_id, например '123'.
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Вызов метода get_operation_receipt

        :param operation_id: Строка с operation_id, например '123'.
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, query: GetOperationQuerySchema) -> GetOperationsResponseSchema:
        """
        Вызов метода get_operations

        :param query: Словарь типа GetOperationQueryDict
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, query: GetOperationQuerySchema) -> GetOperationsSummaryResponseSchema:
        """
        Вызов метода get_operations_summary

        :param query: Словарь типа GetOperationQueryDict
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeResponseSchema:
        """
        Вызов метода make_fee_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpResponseSchema:
        """
        Вызов метода make_top_up_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashBackResponseSchema:
        """
        Вызов метода make_cashback_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashBackResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferResponseSchema:
        """
        Вызов метода make_transfer_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseResponseSchema:
        """
        Вызов метода make_purchase_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillResponseSchema:
        """
        Вызов метода make_bill_payment_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashResponseSchema:
        """
        Вызов метода make_cash_withdrawal_operation

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервера (объект JSON).
        """
        request = MakeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashResponseSchema.model_validate_json(response.text)

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())

def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр AccountsGatewayHTTPClient с хуками сбора метрик.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))
