"""Проверки калькулятора."""

import pytest

from task4 import calculate


@pytest.mark.parametrize(
    ("left", "right", "operation", "expected"),
    [(2, 3, "+", 5), (2, 3, "-", -1), (-2, 3, "*", -6), (7, 2, "/", 3.5)],
)
def test_calculate(
    left: float, right: float, operation: str, expected: float
) -> None:
    """Проверяет четыре арифметические операции."""
    assert calculate(left, right, operation) == expected


def test_division_by_zero() -> None:
    """Проверяет обработку деления на ноль."""
    with pytest.raises(ZeroDivisionError):
        calculate(7, 0, "/")


def test_unknown_operation() -> None:
    """Проверяет обработку неизвестной операции."""
    with pytest.raises(ValueError):
        calculate(7, 2, "%")
