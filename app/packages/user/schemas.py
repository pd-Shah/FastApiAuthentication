from .models import User
from pydantic import BaseModel, Field


class SchemaSignupOutput(BaseModel):
    email: str


class SchemaSignupInput(BaseModel):
    email: str
    password: str


class SchemaLoginInput:
    token: str


class SchemaLoginOutput:
    email: str
    password: str
