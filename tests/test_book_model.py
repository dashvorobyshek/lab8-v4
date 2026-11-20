"""Проверки модели без ввода и вывода."""

import pytest

from book_model import BookModel


def test_add_book() -> None:
    """Проверяет добавление книги и удаление пробелов по краям."""
    model = BookModel()
    model.add_book("  Python  ", 500)
    assert model.get_books() == [("Python", 500)]


@pytest.mark.parametrize(
    ("title", "price"),
    [("", 100), ("   ", 100), ("Python", -1)],
)
def test_invalid_book(title: str, price: int) -> None:
    """Проверяет, что неверные данные не изменяют список."""
    model = BookModel()
    with pytest.raises(ValueError):
        model.add_book(title, price)
    assert model.get_books() == []


def test_get_books_returns_copy() -> None:
    """Проверяет защиту списка от изменения через результат чтения."""
    model = BookModel()
    model.add_book("Python", 500)
    books = model.get_books()
    books.clear()
    assert model.get_books() == [("Python", 500)]
