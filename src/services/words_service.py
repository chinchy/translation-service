from infrastructure.repositories.words_repository import WordsRepository
from infrastructure.requesters.google_translate_requester import GoogleTranslateRequester
from models.words import WordFilters


class WordsService:
    def __init__(self, words_repository: WordsRepository, google_translate_requester: GoogleTranslateRequester) -> None:
        self._words_repository = words_repository
        self._google_translate_requester = google_translate_requester

    async def get_word(self, word: str):
        ...

    async def delete_word(self, word: str):
        ...

    async def get_words(self, filters: WordFilters):
        ...
