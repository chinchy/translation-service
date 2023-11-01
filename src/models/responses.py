from dataclasses import dataclass

from models.words import Word


@dataclass
class SingleWord:
    item: Word


@dataclass
class SingleWordResponse:
    data: SingleWord


@dataclass
class PaginatedWords:
    items: list[Word]
    total_item_count: int
    page: int
    per_page: int
    page_count: int


@dataclass
class PaginatedWordsResponse:
    data: PaginatedWords
