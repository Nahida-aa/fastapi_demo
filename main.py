from typing import Annotated
from fastapi import Depends, FastAPI
from apps.users import router as users_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users_router.router)

