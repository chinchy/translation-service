import logging

import inject
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from infrastructure.repositories.words_repository import WordsRepository
from infrastructure.requesters.google_translate_requester import GoogleTranslateRequester
from routers.words_router import router as words_router
from services.words_service import WordsService
from settings import Settings

logging.basicConfig(level=Settings.APP_LOG_LEVEL)

app = FastAPI(default_response_class=ORJSONResponse)
app.include_router(words_router)

pg_engine: AsyncEngine | None = None


def config(binder):
    global pg_engine

    # PostgreSQL
    pg_engine = create_async_engine(
        Settings.get_pg_url(),
        pool_size=Settings.PG_POOL_SIZE,
        pool_recycle=Settings.PG_POOL_RECYCLE,
        pool_timeout=Settings.PG_POOL_TIMEOUT,
        connect_args=Settings.get_connect_args(),
    )
    words_repository = WordsRepository(pg_engine)
    # ---

    # Requesters
    google_translate_requester = GoogleTranslateRequester()
    # ---

    # Services
    words_service = WordsService(
        words_repository=words_repository, google_translate_requester=google_translate_requester
    )
    # ---

    # Binds
    binder.bind(WordsService, words_service)
    # ---


@app.on_event("startup")
async def startup_event():
    inject.configure(config, bind_in_runtime=False)


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Shutting down...")

    assert pg_engine
    await pg_engine.dispose()
