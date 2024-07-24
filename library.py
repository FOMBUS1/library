from book import Book
from typing import Optional
from errors import *

import json

class Library():
    def __init__(self):
        self.books: list[Book] = list()

    def add(self, title: str, author: str, year: int) -> None:
        book = Book(len(self.books)+1, title, author, year, "В наличие")
        self.books.append(book)

    def remove(self, bid: int) -> None:
        if bid < 1 or bid > len(self.books):
            raise OutOfBounds("Id must be in range [1, len(Library)]")
        
        book = self.__find_by_inx(bid)
        self.books.remove(book)
        
    def find(self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None) -> list[Book]:
        output_books = []
        for book in self.books:
            if title is not None and author is not None and year is not None:
                if book.title == title and book.author == author and book.year == year:
                        output_books.append(book)
            elif title is not None and author is not None:
                if book.title == title and book.author == author:
                        output_books.append(book)
            elif title is not None and year is not None:
                if book.title == title and book.year == year:
                        output_books.append(book)
            elif author is not None and year is not None:
                if book.author == author and book.year == year:
                        output_books.append(book)
            elif title is not None:
                if book.title == title:
                        output_books.append(book)
            elif author is not None:
                if book.author == author:
                        output_books.append(book)
            elif year is not None:
                 if book.year == year:
                        output_books.append(book)
            else:
                raise InvalidArguments("No arguments were given")
        return output_books


    def __find_by_inx(self, inx: int) -> Book:
        for book in self.books:
            if book.id == inx:
                return book

    def set_status(self, inx: int, status: str) -> None:
        stat = ['В наличие', 'Выдана']
        if status not in stat:
            raise InvalidStatus("Invalid status!") 
        self.__find_by_inx(inx).status = status

    def to_json(self):
        book_dict = {"books": []}
        for book in self.books:
            book_dict['books'].append({'bid': book.bid,
             'title': book.title,
             'author': book.author,
             'year': book.year,
             'status': book.status})
        book_dict = json.dumps(book_dict)
        return book_dict
    
    def save(self, path_to_save: str) -> None:
        json = self.to_json()
        with open(path_to_save, 'w') as f:
            f.write(json)        
             
    @staticmethod
    def load_from_json(path: str):
        with open(path, 'rb') as f:
            books = json.loads(f.read())

        lib = Library()
        for inx, book in enumerate(books['books']):
            lib.add(book.title, book.author, book.year)
            lib.set_status(inx, book.status)
        
        return lib
    
    def print(self):
        for book in self.books:
            print(book)

    def __len__(self):
        return len(self.books)
