from pydantic import BaseModel


class CreateTeam(BaseModel):
    name: str
    primary_color: str
    secondary_color: str


class CreatedTeam(BaseModel):
    id: int
    name: str
    primary_color: str
    secondary_color: str


class ListTeam(BaseModel):
    id: int
    name: str
    primary_color: str
    secondary_color: str


class CreateEmployee(BaseModel):
    name: str
    role: str
    image: str
    team_id: int


class CreatedEmployee(BaseModel):
    id: int
    name: str
    role: str
    image: str
    team_id: int


class ListEmployee(BaseModel):
    id: int
    name: str
    role: str
    image: str
    team_id: int
