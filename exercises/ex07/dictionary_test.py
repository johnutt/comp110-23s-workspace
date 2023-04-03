"""Unit Tests for Exercise07!"""
__author__ = 730579193


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_use_case_1() -> None:
    """Tests invert function with a typical use case."""
    input: dict[str, str] = {"eddie": "cheeseburger", "frank": "hotdog", "bob": "french fries"}
    assert invert(input) == {"cheeseburger": "eddie", "hotdog": "frank", "french fries": "bob"}


def test_invert_use_case_2() -> None:
    """Tests invert function with a typical use case."""
    input: dict[str, str] = {"chuck": "green", "joe": "purple", "polly": "yellow"}
    assert invert(input) == {"green": "chuck", "purple": "joe", "yellow": "polly"}


def test_invert_edge_case_1() -> None:
    """Tests invert function with same keys."""
    input: dict[str, str] = {"george": "george", "bruce": "bruce"}
    assert invert(input) == {"george": "george", "bruce": "bruce"}


def test_favorite_color_use_case_1() -> None:
    input: dict[str, str] = {"chuck": "green", "joe": "green", "polly": "yellow"}
    assert favorite_color(input) == "green"
    """Tests favorite color function with a typical use case."""


def test_favorite_color_use_case_2() -> None:
    """Tests favorite color function with a typical use case."""
    input: dict[str, str] = {"leo": "red", "miles": "blue", "bill": "red"}
    assert favorite_color(input) == "red"


def test_favorite_color_edge_case_1() -> None:
    """Tests favorite color function with an edge case."""
    input: dict[str, str] = {"leo": "yellow", "miles": "blue", "bill": "purple"}
    assert favorite_color(input) == "yellow"


def test_count_use_case_1() -> None:
    """Tests count function with a typical use case."""
    input: list[str] = ["chocolate", "vanilla", "chocolate", "strawberry"]
    assert count(input) == {"chocolate": 2, "vanilla": 1, "strawberry": 1}


def test_count_use_case_2() -> None:
    """Tests count function with a typical use case."""
    input: list[str] = ["ed", "ben", "steve", "ben"]
    assert count(input) == {"ed": 1, "ben": 2, "steve": 1}


def test_count_edge_case_1() -> None:    
    """Tests count function with an edge case."""
    input: list[str] = ["baseball"]
    assert count(input) == {"baseball": 1}