import uuid
import httpx
import uvicorn
from fastapi import FastAPI, Response
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse


app = FastAPI()

url_store = {}  # хранение короткого и оригинального URL


class RequestURL(BaseModel):
    """Объект URL"""
    url: str


@app.post("/", status_code=status.HTTP_201_CREATED)
async def short_url(url_request: RequestURL, response: Response):
    """Создаем уникальное значение в 6 знаков и присваеваем оригинальному URL"""
    url_short = str(uuid.uuid4())[:6]
    url_store[url_short] = url_request.url

    response.status_code = status.HTTP_201_CREATED
    return JSONResponse(content=f"127.0.0.1:8000/{url_short}")


@app.get("/{url_short}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def original_url(url_short: str):
    """Возвращаем оригинальный URL"""

    return {"Location": url_store[url_short]}


@app.get("/async/{url_short}")
async def async_request(url_short: str):
    """Обращаемся по короткому URL, возвращаем полученные данные"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://127.0.0.1:8000/{url_short}")
        external_data = response.json()

    return JSONResponse(
        content={
            "url_short": url_short,
            "original_url": url_store[url_short],
            "external_data": external_data,
            "message": "Данные получены",
        },
        status_code=status.HTTP_200_OK,
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
