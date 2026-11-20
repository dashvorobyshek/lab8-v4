"""Контроллер приложения со списком книг."""

from book_model import BookModel
from book_view import BookView


class BookController:
    """Связывает действия пользователя, модель и представление."""

    def __init__(self, model: BookModel, view: BookView) -> None:
        """Получает модель и представление приложения."""
        self.model = model
        self.view = view

    def run(self) -> None:
        """Обрабатывает действия до выбора выхода."""
        while True:
            action = self.view.choose_action()

            if action == "0":
                return
            if action == "1":
                self.view.show_books(self.model.get_books())
            elif action == "2":
                title, price_text = self.view.read_book()
                try:
                    price = int(price_text)
                except ValueError:
                    self.view.show_message("Цена должна быть целым числом.")
                    continue

                try:
                    self.model.add_book(title, price)
                except ValueError as error:
                    self.view.show_message(str(error))
                else:
                    self.view.show_message("Книга добавлена.")
            else:
                self.view.show_message("Выберите 1, 2 или 0.")
