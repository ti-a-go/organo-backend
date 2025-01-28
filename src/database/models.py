from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    primary_color: Mapped[str] = mapped_column(String(9))
    secondary_color: Mapped[str] = mapped_column(String(9))

    employees: Mapped["Employee"] = relationship(back_populates="team")


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    role: Mapped[str] = mapped_column(String(50))
    image: Mapped[str] = mapped_column(String(150))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))

    team: Mapped["Team"] = relationship(back_populates="employees")
