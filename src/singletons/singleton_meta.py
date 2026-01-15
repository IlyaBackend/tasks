class SingletonMeta(type):
    """Singleton реализация при помощи метакласса."""

    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        print("Logger initialized")


l1 = Logger()
l2 = Logger()

assert l1 is l2
