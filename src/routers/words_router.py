import inject
from fastapi import APIRouter, Depends, Query
from fastapi.responses import ORJSONResponse

from models.responses import PaginatedWordsResponse, SingleWordResponse
from models.words import WordFilters
from services.words_service import WordsService
from utils.response import paginated_items, single_item

router = APIRouter(prefix="/words", tags=["Words"])


def get_words_service() -> WordsService:
    return inject.instance(WordsService)


@router.get("/{word}", response_model=SingleWordResponse)
async def get_word(word: str, service: WordsService = Depends(get_words_service)) -> ORJSONResponse:
    result = await service.get_word(word)
    return single_item(result)


@router.delete("/{word}", response_model=SingleWordResponse)
async def delete_word(word: str, service: WordsService = Depends(get_words_service)) -> ORJSONResponse:
    result = await service.delete_word(word)
    return single_item(result)


@router.get("", response_model=PaginatedWordsResponse)
async def get_words(
    search_string: str | None = Query(None, alias="q", description="Partial match for filtering"),
    definitions: bool = Query(False),
    synonyms: bool = Query(False),
    translations: bool = Query(False),
    page: int = Query(0, ge=0, le=1000),
    per_page: int = Query(10, ge=1, le=1000),
    service: WordsService = Depends(get_words_service),
) -> ORJSONResponse:
    result, total_item_count = await service.get_words(
        WordFilters(
            search_string=search_string,
            definitions=definitions,
            synonyms=synonyms,
            translations=translations,
            page=page,
            per_page=per_page,
        )
    )
    return paginated_items(result, total_item_count=total_item_count, page=page, per_page=per_page)
