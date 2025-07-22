from pydantic import BaseModel


class Card(BaseModel):
    card_id: int
    question: str
    answer: str


    class Config:
        allow_mutation = True
