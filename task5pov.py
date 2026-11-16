from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(title="Подсчёт слов")


class TextRequest(BaseModel):
    """Текст, в котором нужно посчитать слова."""

    model_config = ConfigDict(str_strip_whitespace=True)

    text: str = Field(min_length=1)


@app.post("/words/count")
def count_words(data: TextRequest) -> dict[str, int]:
    """Считает части текста, разделённые пробельными символами."""
    return {"count": len(data.text.split())}
