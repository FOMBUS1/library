from dataclasses import dataclass

@dataclass(slots=True)
class Book:
    bid: int
    title: str
    author: str
    year: int
    status: str

