import inject
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from starlette import status

from models.responses import SingleWordResponse, PaginatedWordsResponse
from services.words_service import WordsService

router = APIRouter(prefix="/words", tags=["Words"])


def get_words_service() -> WordsService:
    return inject.instance(WordsService)


@router.get("/{word}", response_model=SingleWordResponse)
async def get_word(service: WordsService = Depends(get_words_service)) -> ORJSONResponse:
    result = await service.get_word()
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={"data": {"item": result}}
    )


@router.delete("/{word}", response_model=SingleWordResponse)
async def delete_word(service: WordsService = Depends(get_words_service)) -> ORJSONResponse:
    result = await service.delete_word()
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={"data": {"item": result}}
    )


@router.get("", response_model=PaginatedWordsResponse)
async def get_words(service: WordsService = Depends(get_words_service)) -> ORJSONResponse:
    result = await service.get_words()
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={"data": {"item": result}}
    )
