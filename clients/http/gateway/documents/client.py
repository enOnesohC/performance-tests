from httpx import Response
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from typing import TypedDict


class DocumentDict:
    """
    Описание структуры документа
    """
    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа получения тарифа документа
    """
    tariff: DocumentDict


class GetContractDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа получения контракта документа
    """
    contract: DocumentDict


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить документ тарифа по счету через апи.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить документ контракта по счету через апи.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получить документ тарифа

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получить документ контракта

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект JSON).
        """
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
