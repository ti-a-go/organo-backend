import os
from typing import Annotated

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import Session
from fastapi import Depends


load_dotenv()


CONNECTION_URL = URL.create(
    os.getenv("DATABASE_ENGINE"),
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT"),
    database=os.getenv("DATABASE_NAME"),
    username=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
)

if os.getenv("DEBUG") == "true":
    echo = True


engine = create_engine(CONNECTION_URL, echo=echo)


def get_session():
    with Session(engine) as session:
        yield session


DBSession = Annotated[Session, Depends(get_session)]
