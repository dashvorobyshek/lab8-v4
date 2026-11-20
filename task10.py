from book_controller import BookController
from book_model import BookModel
from book_view import BookView


def main() -> None:
    """Создаёт компоненты MVC и запускает приложение."""
    model = BookModel()
    view = BookView()
    controller = BookController(model, view)
    controller.run()


if __name__ == "__main__":
    main()
