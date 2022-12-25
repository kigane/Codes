import inspect
import json
from dataclasses import asdict, astuple, dataclass, field
from typing import List, Optional

import pydantic

data = [
    {
        "title": "Zero to One",
        "subtitle": "Notes on Startups, or How to Build the Future",
        "author": "Peter Thiel",
        "publisher": "Ballantine Books",
        "isbn_10": "0753555190",
        "isbn_13": "978-0753555194",
        "price": 14.29,
        "author2": {
            "name": "Peter Thiel",
            "verified": True
        }
    },
    {
        "title": "The Lean Startup",
        "subtitle": "How Relentless Change Creates Radically Successful Businesses",
        "author": "Eric Ries",
        "publisher": "Penguin UK",
        "isbn_10": "0670921602",
        "isbn_13": "978-0670921607",
        "price": 12.96
    },
    {
        "title": "A Promised Land",
        "author": "Barack Obama",
        "publisher": "Viking UK",
        "isbn_10": "0241491517",
        "isbn_13": "978-0241491515",
        "price": 31.74
    },
    {
        "title": "The Hard Thing about Hard Things",
        "subtitle": "Building a Business When There Are No Easy Answers",
        "author": "Ben Horowitz",
        "publisher": "HarperBusiness",
        "isbn_10": "0062273205",
        "isbn_13": "978-0062273208",
        "price": 15.55
    },
    {
        "title": "Design patterns",
        "subtitle": "Elements of reusable object-oriented software",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "publisher": "Addison Wesley",
        "isbn_10": "0201633612",
        "isbn_13": "978-0201633610",
        "price": 50
    },
    {
        "title": "Clean Code",
        "subtitle": "A Handbook of Agile Software Craftsmanship",
        "author": "Robert Martin",
        "publisher": "Financial Times Prentice Hall",
        "isbn_10": "0132350882",
        "isbn_13": "978-0132350884",
        "price": 33.43
    }
]


class ISBNMissingError(Exception):
    """Custom error that is raised when both ISBN10 and ISBN13 are missing."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 doesn't have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Author(pydantic.BaseModel):
    name: str
    verified: bool


class Book(pydantic.BaseModel):
    """Represents a book with that you can read from a JSON file."""

    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    author2: Optional[Author]

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn_10_or_13(cls, values):
        """Make sure there is either an isbn_10 or isbn_13 value defined"""
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should have either an ISBN10 or ISBN13",
            )
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None:
        """Validator to check whether ISBN10 is valid"""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(
                value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value

    class Config:
        """Pydantic config class"""

        allow_mutation = False
        anystr_lower = True


def main() -> None:
    """Main function."""

    books: List[Book] = [Book(**item) for item in data]
    # print(books)
    print(type(books[1].json()))
    # print(books[0].dict(exclude={"price"}))
    # print(books[1].copy())


if __name__ == "__main__":
    main()
