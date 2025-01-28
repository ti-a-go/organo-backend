from src.database.session import DBSession
from src.api.models import (
    CreateTeam,
    CreatedTeam,
    ListTeam,
    CreatedEmployee,
    CreateEmployee,
    ListEmployee,
)
from src.database.models import Team, Employee
from sqlalchemy import select


def create_team_controller(db: DBSession, data: CreateTeam):
    new_team = Team(
        name=data.name,
        primary_color=data.primary_color,
        secondary_color=data.secondary_color,
    )

    db.add(new_team)
    db.commit()
    db.refresh(new_team)

    return CreatedTeam(
        id=new_team.id,
        name=new_team.name,
        primary_color=new_team.primary_color,
        secondary_color=new_team.secondary_color,
    )


def list_teams_controller(db: DBSession, page: int | None, page_size: int | None):
    if page is None:
        page = 1
    if page_size is None:
        page_size = 100

    offset = (page - 1) * page_size
    limit = page_size
    statement = select(Team).offset(offset).limit(limit)

    result = db.execute(statement).scalars().all()

    return [
        ListTeam(
            id=team.id,
            name=team.name,
            primary_color=team.primary_color,
            secondary_color=team.secondary_color,
        )
        for team in result
    ]


def create_employee_controller(db: DBSession, data: CreateEmployee):
    team = db.execute(select(Team).where(Team.id == data.team_id)).scalar()

    if team is None:
        return None

    new_employee = Employee(
        name=data.name,
        role=data.role,
        image=data.image,
        team_id=data.team_id,
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return CreatedEmployee(
        id=new_employee.id,
        name=new_employee.name,
        role=new_employee.role,
        image=new_employee.image,
        team_id=new_employee.team_id,
    )


def list_employee_controller(db: DBSession, page: int | None, page_size: int | None):
    if page is None:
        page = 1
    if page_size is None:
        page_size = 100

    offset = (page - 1) * page_size
    limit = page_size
    statement = select(Employee).offset(offset).limit(limit)

    result = db.execute(statement).scalars().all()

    return [
        ListEmployee(
            id=employee.id,
            name=employee.name,
            role=employee.role,
            image=employee.image,
            team_id=employee.team_id,
        )
        for employee in result
    ]
