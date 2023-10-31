from dataclasses import dataclass


@dataclass
class SingleWord:
    item: ...


@dataclass
class SingleWordResponse:
    data: SingleWord


@dataclass
class PaginatedWords:
    items: ...


@dataclass
class PaginatedWordsResponse:
    data: PaginatedWords
