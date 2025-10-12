from pydantic import BaseModel


class DocumentSchema(BaseModel):
    """
    Описание структуры документа
    """
    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения тарифа документа
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения контракта документа
    """
    contract: DocumentSchema
