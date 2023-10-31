from typing import Any
from uuid import uuid4

from asyncpg import Connection
from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()


class CConnection(Connection):
    def _get_unique_id(self, prefix: str) -> str:
        return f"__asyncpg_{prefix}_{uuid4()}__"


class Settings:
    # Constants
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = SECONDS_IN_MINUTE * 60

    # PostgreSQL
    PG_HOST = env.str("PG_HOST")
    PG_PORT = env.int("PG_PORT", 5432)
    PG_USER = env.str("PG_USER")
    PG_PASSWORD = env.str("PG_PASSWORD")
    PG_DB = env.str("PG_DB")

    PG_MIGRATE_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

    PG_POOL_RECYCLE = env.int("POOL_RECYCLE", SECONDS_IN_HOUR)
    PG_PREPARED_STATEMENT = env.bool("PG_PREPARED_STATEMENT", True)

    PG_POOL_SIZE = env.int("PG_POOL_SIZE", 8)
    PG_POOL_TIMEOUT = env.int("PG_POOL_TIMEOUT", 5)
    PG_CONN_TIMEOUT = env.int("PG_CONN_TIMEOUT", 5)
    PG_COMMAND_TIMEOUT = env.int("PG_COMMAND_TIMEOUT", 5)

    # Httpx
    HTTP_TIMEOUT = env.int("HTTP_TIMEOUT", 10)
    MAX_CONNECTIONS = env.int("MAX_CONNECTIONS", 100)
    MAX_KEEPALIVE_CONNECTIONS = env.int("MAX_KEEPALIVE_CONNECTIONS", 20)
    KEEPALIVE_EXPIRY = env.int("KEEPALIVE_EXPIRY", 1800)

    # Logging
    APP_LOG_LEVEL = env.log_level("APP_LOG_LEVEL", "INFO")

    @classmethod
    def get_pg_url(cls) -> str:
        return (
            f"postgresql+asyncpg://:@?dsn=postgresql://:@{cls.PG_HOST}/"
            f"{cls.PG_DB}&port={cls.PG_PORT}&user={cls.PG_USER}&password={cls.PG_PASSWORD}"
        )

    @classmethod
    def get_connect_args(cls) -> dict[str, Any]:
        return {
            "timeout": cls.PG_CONN_TIMEOUT,
            "command_timeout": cls.PG_COMMAND_TIMEOUT,
            "statement_cache_size": 0,
            "prepared_statement_cache_size": 0,
            "connection_class": CConnection,
        }
