from enum import StrEnum
from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class OperationType(StrEnum):
    TOP_UP = "TOP_UP"
    TRANSFER = "TRANSFER"
    WITHDRAWAL = "WITHDRAWAL"

class OperationStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationSchema(BaseModel):
    """
    Структура данных для операций
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: int
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Структура данных для рецепта
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Структура данных для получения списка операций пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: int = Field(alias="spentAmount")
    received_amount: int = Field(alias="receivedAmount")
    cashback_amount: int = Field(alias="cashbackAmount")


class GetOperationQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """
    Структура данных для отправления запроса на платёжные операции
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для отправления запроса на операцию покупки
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=fake.category)


class GetOperationsResponseSchema(BaseModel):
    """
    Структура данных для ответа получения операций
    """
    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура данных для ответа сводки по операциям
    """
    operations: OperationsSummarySchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура данных для ответа по операции
    """
    receipt: OperationReceiptSchema


class GetOperationResponseSchema(BaseModel):
    """
    Структура данных для ответа по получению операции
    """
    operation: OperationSchema


class MakeFeeResponseSchema(BaseModel):
    """
    Структура данных для ответа по операции налога
    """
    operation: MakeOperationRequestSchema


class MakeTopUpResponseSchema(BaseModel):
    """
    Структура данных для ответа по операции создания карты
    """
    operation: MakeOperationRequestSchema


class MakeCashBackResponseSchema(BaseModel):
    """
    Структура данных для ответа по операции кэшбек
    """
    operation: MakeOperationRequestSchema


class MakeTransferResponseSchema(BaseModel):
    """
    Структура данных для ответа по операции перевода
    """
    operation: MakeOperationRequestSchema


class MakePurchaseResponseSchema(BaseModel):
    """
    Структура данных для ответа по операции покупки
    """
    operation: MakePurchaseOperationRequestSchema


class MakeBillResponseSchema(BaseModel):
    """
    Структура данных для ответа по операции счёта
    """
    operation: MakeOperationRequestSchema


class MakeCashResponseSchema(BaseModel):
    """
    Структура данных для ответа по операции снятия
    """
    operation: MakeOperationRequestSchema
