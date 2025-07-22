from schema_deck import Deck
from schema_flashcards import Flashcards
import model_database # ensure shared db is modified


def create_deck(name: str) -> Deck:
    deck = Deck(deck_id=name, cards=[])
    model_database.db[name] = deck
    return deck


def read_all_decks() -> Flashcards:
    return Flashcards(flashcards=model_database.db)


def read_deck(name: str) -> Deck:
    deck = model_database.db.get(name)
    return deck


def update_deck(old_name: str, new_name: str) -> Deck:
    deck = model_database.db[old_name]
    model_database.db[new_name] = deck
    deck.deck_id = new_name
    return deck


def delete_deck(name: str) -> Deck:
    deck = model_database.db.get(name)
    del model_database.db[name]
    return deck
