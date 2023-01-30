from .models import User

def signup_logic(user, ):
    new_user = User.create(email=user.email, password=user.password)
    new_user.save()
    return new_user
