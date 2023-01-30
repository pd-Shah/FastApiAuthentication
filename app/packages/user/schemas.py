from .models import User
from pydantic import BaseModel, Field


class SchemaSignupOutput(BaseModel):
    email: str


class SchemaSignupInput(BaseModel):
    email: str
    password: str


class SchemaLoginOutput(BaseModel):
    token: str


class SchemaLoginInput(BaseModel):
    email: str
    password: str
