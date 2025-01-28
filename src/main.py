from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers import teams_router, employees_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teams_router)
app.include_router(employees_router)


@app.get("/")
async def root():
    return {"message": "Backend api for Organo App."}
