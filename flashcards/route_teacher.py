from fastapi import APIRouter
from schema_deck import Deck
from schema_flashcards import Flashcards
from service_deck import create_deck, read_all_decks, read_deck, update_deck, delete_deck


router = APIRouter(prefix="/teacher", tags=["Teacher"])


# use plural nouns for resources
@router.post(path="/decks", response_model=Deck)
def create_deck_route(name: str) -> Deck:
    """
    curl -X POST "http://127.0.0.1:8000/teacher/decks?name=Geometry" \
     -H "accept: application/json"
    """
    return create_deck(name)


@router.get(path="/decks", response_model=Flashcards)
def read_all_decks_route() -> Flashcards:
    """
    curl -X GET "http://127.0.0.1:8000/teacher/decks" \
     -H "accept: application/json"
    """
    return read_all_decks()


@router.get(path="/decks/{name}", response_model=Deck)
def read_deck_route(name: str) -> Deck:
    """
    curl -X GET "http://127.0.0.1:8000/teacher/decks/Geography" \
     -H "accept: application/json"
    """
    return read_deck(name)


@router.put(path="/decks/{old_name}", response_model=Deck)
def update_deck_route(old_name: str, new_name: str) -> Deck:
    """
    curl -X PUT "http://127.0.0.1:8000/teacher/decks/Geometry?new_name=Algebra" \
     -H "accept: application/json"
    """
    return update_deck(old_name, new_name)


@router.delete(path="/decks/{name}", response_model=Deck)
def delete_deck_route(name: str) -> Deck:
    """
    curl -X DELETE "http://127.0.0.1:8000/teacher/decks/Geometry" \
     -H "accept: application/json"
    """
    return delete_deck(name)
