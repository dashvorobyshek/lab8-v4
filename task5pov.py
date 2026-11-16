"""Заготовка API для этапа Red."""

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/words/count")
def count_words() -> dict[str, int]:
    """Обозначает маршрут до реализации."""
    raise HTTPException(status_code=501, detail="Пока не реализовано")
