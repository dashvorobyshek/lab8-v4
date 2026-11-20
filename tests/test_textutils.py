"""Проверки функции пакета."""

import pytest

from lab8_textutils import normalize_spaces


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("  Привет   мир  ", "Привет мир"),
        ("раз\tдва\nтри", "раз два три"),
        ("", ""),
        (" \t\n ", ""),
    ],
)
def test_normalize_spaces(text: str, expected: str) -> None:
    """Проверяет пробелы по краям, табуляцию и пустые строки."""
    assert normalize_spaces(text) == expected
