from pydantic import BaseModel, Field, EmailStr


class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя
    """
    email: EmailStr = "user@example.com"
    last_name: str = Field(alias="lastName", default="lastName")
    first_name: str = Field(alias="firstName", default="firstName")
    middle_name: str = Field(alias="middleName", default="middleName")
    phone_number: str = Field(alias="phoneNumber", default="888003535")


class UserShema(CreateUserRequestSchema):
    """
    Модель данных пользователя
    """
    id: str = "user-id"


class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя
    """
    user: UserShema
