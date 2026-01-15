class Singleton:
    """Реализация Singleton при помощи метода __new__."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None, time=None):
        if not hasattr(self, "_initialized"):
            self.value = value
            self.time = time
            self._initialized = True


obj1 = Singleton(10, 14)
obj2 = Singleton(20, 15)
obj3 = Singleton(30, 22)


assert obj1 is obj2
