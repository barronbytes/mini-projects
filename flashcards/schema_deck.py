from pydantic import BaseModel, Field
from schema_card import Card


class Deck(BaseModel):
    deck_id: str
    cards: list[Card] = Field(default_factory=list)


    class Config:
        allow_mutation = True
