
from fastapi import FastAPI
from settings import config
from tortoise.contrib.fastapi import register_tortoise
from app.packages.user.models import User
from app.packages.user import router as user_router

# Factory method to make a Flask app
app = FastAPI(
    import_name=__name__,
    instance_relative_config=True,
)

# register applications
app.include_router(user_router, prefix='/user')

# config db
register_tortoise(app=app, generate_schemas=True, add_exception_handlers=True, db_url='sqlite://instance/db.db', modules={'models':['app']})


