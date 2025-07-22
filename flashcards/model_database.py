from schema_card import Card
from schema_deck import Deck


db = {
    "Geography": Deck(
        deck_id="Geography",
        cards=[
            Card(card_id=1, question="What state is written as GA?", answer="Georgia"),
            Card(card_id=2, question="What state is written as FL?", answer="Florida")
        ]
    )
}
