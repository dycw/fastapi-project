from fastapi import FastAPI

from app.db import User, database

app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/")
async def read_root() -> list[User]:
    return await User.objects.all()


@app.on_event("startup")
async def startup() -> None:
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    _, _ = await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown() -> None:
    if database.is_connected:
        await database.disconnect()
