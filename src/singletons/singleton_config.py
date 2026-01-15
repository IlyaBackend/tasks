class Config:
    """Своего рода Singleton для реализации в будующих модулях."""

    def __init__(self):
        self.debug = False
        self.db_url = "sqlite:///:memory:"


config = Config()
