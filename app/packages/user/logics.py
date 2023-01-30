from .models import User

async def signup_logic(user, ):
    new_user = await User.create(email=user.email, password=user.password)
    await new_user.save()
    return new_user


async def login_logic(user, ):
    email = user.email
    password = user.password
    result = {'token': None}

    # get user by email
    u = await User.get(email=email)
    if u.verify_password(password):
        # then make a token
        result['token'] = u.generate_token()

    return result