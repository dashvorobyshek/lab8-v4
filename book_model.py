"""Модель приложения со списком книг."""


class BookModel:
    """Хранит книги в памяти и проверяет их данные."""

    def __init__(self) -> None:
        """Создаёт пустой список книг."""
        self._books: list[tuple[str, int]] = []

    def add_book(self, title: str, price: int) -> None:
        """Добавляет книгу с непустым названием и неотрицательной ценой."""
        title = title.strip()
        if not title:
            raise ValueError("Название книги не должно быть пустым.")
        if price < 0:
            raise ValueError("Цена не должна быть отрицательной.")
        self._books.append((title, price))

    def get_books(self) -> list[tuple[str, int]]:
        """Возвращает копию списка книг."""
        return self._books.copy()
