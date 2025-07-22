from pydantic import BaseModel
from schema_deck import Deck


class Flashcards(BaseModel):
    flashcards: dict[str, Deck]
