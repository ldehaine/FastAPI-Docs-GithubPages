import json

from fastapi import FastAPI, HTTPException
from fastapi.openapi.models import Response

from pydantic import BaseModel, conint

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}


@my_awesome_api.get("/greet", tags=["Greet"])
async def greet_with_my_name(name: str = "Dear"):
    return {"message": f"Hello {name}"}
