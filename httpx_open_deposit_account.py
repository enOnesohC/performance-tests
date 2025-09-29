import httpx
import time


URL_USER = "http://localhost:8003/api/v1/users"
URL_DEPOSIT = "http://localhost:8003/api/v1/accounts/open-deposit-account"


def create_user():
    user = {
        "email": f"user.{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"
    }

    response = httpx.post(URL_USER, json=user)
    result = response.json()

    print(result)
    print(response.status_code)

    return result


def create_deposit(result):
    deposit = {
        "userId": f"{result['user']['id']}"
    }

    response = httpx.post(URL_DEPOSIT, json=deposit)
    result = response.json()

    print(result)
    print(response.status_code)

    return result


create_deposit(create_user())
