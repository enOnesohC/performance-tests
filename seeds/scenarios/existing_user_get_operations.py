from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который выполняет операцию покупки.
    Создаёт 300 пользователей, каждому открывает кредитный счёт, совершает 5 операций покупок,
    1 операцию пополнения счёта, 1 операцию снятия наличных
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга, который описывает, сколько пользователей нужно создать
        и какие именно данные для них генерировать.
        В данном случае создаём 300 пользователей, каждому открываем кредитный счёт,
        совершаем 5 операций покупок,
        1   операцию пополнения счёта, 1 операцию снятия наличных
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Количество пользователей
                credit_card_accounts=SeedAccountsPlan(
                    count=1,  # Количество счётов на пользователя
                    purchase_operations=SeedOperationsPlan(count=5), # Количество операций покупок
                    top_up_operations=SeedOperationsPlan(count=1), # Количество операций пополнения счёта
                    cash_withdrawal_operations=SeedOperationsPlan(count=1) # Количество операций снятия наличных
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_get_operations"


if __name__ == "__main__":
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
