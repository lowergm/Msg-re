from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
from router import router
from tortoise.contrib.fastapi import register_tortoise

load_dotenv()
db_url = os.getenv("DB_URL",  "sqlite://db.sqlite3")

app = FastAPI(
    docs_url=None,
    redoc_url=None
)
app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")

register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
