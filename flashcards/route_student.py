from fastapi import APIRouter
from schema_deck import Deck
from schema_flashcards import Flashcards
from service_deck import read_all_decks, read_deck


router = APIRouter(prefix="/student", tags=["Student"])


# use plural nouns for resources
@router.get(path="/decks", response_model=Flashcards)
def read_all_decks_route() -> Flashcards:
    return read_all_decks()


@router.get(path="/decks/{name}", response_model=Deck)
def read_deck_route(name: str) -> Deck:
    return read_deck(name)
