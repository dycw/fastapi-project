import datetime as dt

from beartype import beartype
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from utilities.zoneinfo import HONG_KONG

from app import VERSION
from app.config import ENVIRONMENT

templates = Jinja2Templates(directory="templates")


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
@beartype
async def home(*, request: Request) -> Response:
    try:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "datetime": dt.datetime.now(tz=HONG_KONG),
                "environment": ENVIRONMENT,
                "version": VERSION,
            },
        )
    except Exception as error:  # noqa: BLE001
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        ) from None
