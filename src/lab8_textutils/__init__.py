"""Функции для работы с текстом."""


def normalize_spaces(text: str) -> str:
    """Заменяет группы пробельных символов одним пробелом."""
    return " ".join(text.split())
