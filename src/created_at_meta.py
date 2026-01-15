from datetime import datetime


class CreatedAtMeta(type):
    """
    Мета класс для добавления к любоу наследнику
    поля created_at с текущей датой и временем.
    """

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        cls.created_at = datetime.now()
        return cls
