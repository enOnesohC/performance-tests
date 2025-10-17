from grpc import Channel

from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptResponse,
    GetOperationReceiptRequest
)
from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationResponse,
    MakeTopUpOperationRequest
)
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryResponse,
    GetOperationsSummaryRequest
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationResponse,
    MakeCashWithdrawalOperationRequest
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse
)

class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationGatewayService.
    Предоставляет высокоуровневые методы для работы с операциями.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)

        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов метода GetOperation через gRPC.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ от сервиса с данными об операции с operation_id
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов метода GetOperationReceipt через gRPC.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ от сервиса с данными о чеке по операции с operation_id
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов метода GetOperations через gRPC.

        :param request: gRPC-запрос с ID аккаунта.
        :return: Ответ от сервиса с данными списка операций для определённого счёта
        """
        return self.stub.GetOperations(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов метода GetOperationsSummary через gRPC.

        :param request: gRPC-запрос с ID аккаунта.
        :return: Ответ от сервиса с данными об операции.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов метода MakeFeeOperation через gRPC.

        :param request: gRPC-запрос с ID карты, ID аккаунта, статусом, количеством
        :return: Ответ от сервиса с данными об операции.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов метода MakeTopUpOperation через gRPC.

        :param request: gRPC-запрос с ID карты, ID аккаунта, статусом, количеством
        :return: Ответ от сервиса с данными об операции.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashbackOperation через gRPC.

        :param request: gRPC-запрос с ID карты, ID аккаунта, статусом, количеством
        :return: Ответ от сервиса с данными об операции.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов метода MakeTransferOperation через gRPC.

        :param request: gRPC-запрос с ID карты, ID аккаунта, статусом, количеством
        :return: Ответ от сервиса с данными об операции.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов метода MakePurchaseOperation через gRPC.

        :param request: gRPC-запрос с ID карты, ID аккаунта, статусом, количеством, категорией
        :return: Ответ от сервиса с данными об операции.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов метода MakeBillPaymentOperation через gRPC.

        :param request: gRPC-запрос с ID карты, ID аккаунта, статусом, количеством
        :return: Ответ от сервиса с данными об операции.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashWithdrawalOperation через gRPC.

        :param request: gRPC-запрос с ID карты, ID аккаунта, статусом, количеством
        :return: Ответ от сервиса с данными об операции.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operation(self, operation_id) -> GetOperationResponse:
        """
        Высокоуровневый вызов метода GetOperation через gRPC

        :param operation_id: строка, ID операции
        :return: Ответ от сервиса с данными об операции.
        """
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)


    def get_operation_receipt(self, operation_id) -> GetOperationReceiptResponse:
        """
        Высокоуровневый вызов метода GetOperationReceipt через gRPC

        :param operation_id: строка, ID операции
        :return: Ответ от сервиса с данными об операции.
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id) -> GetOperationsResponse:
        """
        Высокоуровневый вызов метода GetOperations через gRPC

        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса с данными об операциям
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id) -> GetOperationsSummaryResponse:
        """
        Высокоуровневый вызов метода GetOperationsSummary через gRPC

        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса со сводкой по операциям
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id, account_id) -> MakeFeeOperationResponse:
        """
        Высокоуровневый вызов метода MakeFeeOperation через gRPC

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса с данными об операции.
        """
        request = MakeFeeOperationRequest(card_id=card_id,
                                          account_id=account_id,
                                          amount=fake.amount(),
                                          status=fake.proto_enum(OperationStatus))
        return self.make_fee_operation_api(request)

    def make_top_up_operation (self, card_id, account_id) -> MakeTopUpOperationResponse:
        """
        Высокоуровневый вызов метода MakeTopUpOperation через gRPC

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса с данными об операции.
        """
        request = MakeTopUpOperationRequest(card_id=card_id,
                                            account_id=account_id,
                                            amount=fake.amount(),
                                            status=fake.proto_enum(OperationStatus))
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, card_id, account_id) -> MakeCashbackOperationResponse:
        """
        Высокоуровневый вызов метода MakeCashbackOperation через gRPC

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса с данными об операции.
        """
        request = MakeCashbackOperationRequest(card_id=card_id,
                                               account_id=account_id,
                                               amount=fake.amount(),
                                               status=fake.proto_enum(OperationStatus))
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id, account_id) -> MakeTransferOperationResponse:
        """
        Высокоуровневый вызов метода MakeTransferOperation через gRPC

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса с данными об операции.
        """
        request = MakeTransferOperationRequest(card_id=card_id,
                                               account_id=account_id,
                                               amount=fake.amount(),
                                               status=fake.proto_enum(OperationStatus))
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id, account_id) -> MakePurchaseOperationResponse:
        """
        Высокоуровневый вызов метода MakePurchaseOperation через gRPC

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса с данными об операции.
        """
        request = MakePurchaseOperationRequest(card_id=card_id,
                                               account_id=account_id,
                                               amount=fake.amount(),
                                               status=fake.proto_enum(OperationStatus),
                                               category=fake.category())
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id, account_id) -> MakeBillPaymentOperationResponse:
        """
        Высокоуровневый вызов метода MakeBillPaymentOperation через gRPC

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса с данными об операции.
        """
        request = MakeBillPaymentOperationRequest(card_id=card_id,
                                                  account_id=account_id,
                                                  amount=fake.amount(),
                                                  status=fake.proto_enum(OperationStatus))
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id, account_id) -> MakeCashWithdrawalOperationResponse:
        """
        Высокоуровневый вызов метода MakeCashWithdrawalOperation через gRPC

        :param card_id: строка, идентификатор карты
        :param account_id: строка, идентификатор аккаунта
        :return: Ответ от сервиса с данными об операции.
        """
        request = MakeCashWithdrawalOperationRequest(card_id=card_id,
                                                     account_id=account_id,
                                                     amount=fake.amount(),
                                                     status=fake.proto_enum(OperationStatus))
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())