import httpx
import time


URL_MAIN = "http://localhost:8003"
URL_USERS = "/api/v1/users"
URL_ACCOUNT = "/api/v1/accounts/open-credit-card-account"
URL_PURCHASE = "/api/v1/operations/make-purchase-operation"
URL_RECEIPT = "/api/v1/operations/operation-receipt/"


with httpx.Client(base_url=URL_MAIN) as client:
    data_user = {
        "email": f"user.{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"
    }
    responce_create_user = client.post(URL_USERS, json=data_user)
    print(responce_create_user.status_code)

    data_account = {
        "userId": f"{responce_create_user.json()['user']['id']}"
    }
    response_create_account_card = client.post(URL_ACCOUNT, json=data_account)
    print(response_create_account_card.status_code)

    purchase_data = {
        "status": "IN_PROGRESS",
        "amount": 77.99,
        "category": "taxi",
        "cardId": f"{response_create_account_card.json()['account']['cards'][0]['id']}",
        "accountId": f"{response_create_account_card.json()['account']['cards'][0]['accountId']}"
    }
    response_create_purchase = client.post(URL_PURCHASE, json=purchase_data)
    print(response_create_purchase.status_code)

    response_get_operation_id = client.get(f"{URL_RECEIPT}{response_create_purchase.json()['operation']['id']}")
    print(response_get_operation_id.status_code)
    print(response_get_operation_id.json())
