"""Представление приложения со списком книг."""


class BookView:
    """Получает ввод пользователя и выводит результат."""

    def choose_action(self) -> str:
        """Показывает меню и получает выбранное действие."""
        print("\n1 — Показать книги")
        print("2 — Добавить книгу")
        print("0 — Выйти")
        return input("Выберите действие: ").strip()

    def read_book(self) -> tuple[str, str]:
        """Запрашивает название книги и цену."""
        title = input("Название книги: ")
        price = input("Цена в целых рублях: ")
        return title, price

    def show_books(self, books: list[tuple[str, int]]) -> None:
        """Выводит список книг или сообщение о пустом списке."""
        if not books:
            print("Список книг пока пуст.")
            return
        for number, (title, price) in enumerate(books, start=1):
            print(f"{number}. {title}: {price} руб.")

    def show_message(self, message: str) -> None:
        """Выводит сообщение контроллера."""
        print(message)
