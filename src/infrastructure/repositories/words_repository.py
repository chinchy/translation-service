from sqlalchemy.ext.asyncio import AsyncEngine


class WordsRepository:
    def __init__(self, db: AsyncEngine):
        self._db = db
