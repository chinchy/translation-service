from dataclasses import dataclass


@dataclass
class Word:
    word: str
    definition: list[str]
    synonyms: list[str]
    translations: list[str]


@dataclass
class WordFilters:
    search_string: str | None
    definitions: bool
    synonyms: bool
    translations: bool
    page: int
    per_page: int

    @property
    def limit(self):
        return self.per_page

    @property
    def offset(self):
        return self.page * self.per_page
