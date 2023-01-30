from fastapi import APIRouter
from .schemas import SchemaSignupOutput, SchemaSignupInput, SchemaLoginInput, SchemaLoginOutput
from .logics import signup_logic, login_logic


router = APIRouter()


@router.post('/signup', response_model=SchemaSignupOutput)
async def signup(user: SchemaSignupInput):
    result = signup_logic(user)
    return await result


@router.post('/login', response_model=SchemaLoginOutput)
async def login(user: SchemaLoginInput):
    result = login_logic(user)
    return await result
