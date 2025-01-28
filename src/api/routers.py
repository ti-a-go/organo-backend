from http import HTTPStatus
from fastapi import APIRouter, HTTPException

from src.database.session import DBSession
from src.api.models import CreateTeam, CreatedTeam, CreatedEmployee, CreateEmployee
from src.api.controllers import (
    create_team_controller,
    list_teams_controller,
    create_employee_controller,
    list_employee_controller,
)


teams_router = APIRouter(prefix="/teams")
employees_router = APIRouter(prefix="/employees")


@teams_router.post("/", status_code=HTTPStatus.CREATED, response_model=CreatedTeam)
async def create_team(db: DBSession, data: CreateTeam):
    return create_team_controller(db, data)


@teams_router.get("/")
async def list_teams(
    db: DBSession, page: int | None = None, page_size: int | None = None
):
    return list_teams_controller(db, page, page_size)


@employees_router.post(
    "/", status_code=HTTPStatus.CREATED, response_model=CreatedEmployee
)
async def create_employee(db: DBSession, data: CreateEmployee):
    result = create_employee_controller(db, data)

    if result is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Team not found.")

    return result


@employees_router.get("/")
async def list_employees(
    db: DBSession, page: int | None = None, page_size: int | None = None
):
    return list_employee_controller(db, page, page_size)
