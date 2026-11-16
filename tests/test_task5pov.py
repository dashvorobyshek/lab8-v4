"""Проверки API подсчёта слов."""

from fastapi.testclient import TestClient

from task5pov import app

client = TestClient(app)


def test_count_words() -> None:
    """Проверяет подсчёт слов при лишних пробелах и переносе строки."""
    response = client.post(
        "/words/count",
        json={"text": "  Раз   два\nтри  "},
    )
    assert response.status_code == 200
    assert response.json() == {"count": 3}


def test_blank_text() -> None:
    """Проверяет отклонение строки из пробелов."""
    response = client.post("/words/count", json={"text": "   "})
    assert response.status_code == 422


def test_missing_text() -> None:
    """Проверяет отклонение запроса без поля text."""
    response = client.post("/words/count", json={})
    assert response.status_code == 422
