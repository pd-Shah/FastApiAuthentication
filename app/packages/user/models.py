from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer
from itsdangerous.exc import SignatureExpired, BadSignature
from tortoise import fields
from tortoise.models import Model


class User(Model):
    """
        the user model,
    """
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=128, unique=True, )
    hash_password = fields.CharField(max_length=128, )

    @staticmethod
    def create(email, password,):
        """a solid interface to make an user

        Returns:
            User: an user object
        """
        user = User(email=email)
        user.password = password

        return user

    @property
    def password(self):
        """password property to return error
        Returns:
            AttributeError: password are not allowed to see.
        """
        return AttributeError("[-] passwords are not allowed.")

    @password.setter
    def password(self, passwd):
        """setter to set hash(password)
        Args:
            password (Str): user naked password
        """
        self.hash_password = generate_password_hash(passwd, )

    def verify_password(self, password):
        """to check if the input password hash == db.hash_password
        Args:
            password (Str): user naked password
        Returns:
            bool: T/F if hashes are the same or not
        """
        return check_password_hash(self.hash_password, password)

    @staticmethod
    def get_user(email, ):
        """ get user by email
        """
        return User.get(email=email, )

    def generate_token(self,  ACCESS_TOKEN_EXPIRED_IN=666, SECRET_KEY="SomethingSecret", SALT="dReAmBiG"):
        """generate access token

        Returns:
            access_token
        """
        access_token_serializer = TimedJSONWebSignatureSerializer(
            secret_key=SECRET_KEY,
            salt=SALT,
            expires_in=ACCESS_TOKEN_EXPIRED_IN, )

        return access_token_serializer.dumps(
            {'code': self.id, }
        ).decode('UTF-8')

    def validate_token(self, token, SECRET_KEY="SomethingSecret", SALT="dReAmBiG"):
        """ valitate if the token is fine or what

        Returns:
            True/False
        """
        result = False
        serializer = TimedJSONWebSignatureSerializer(
            secret_key=SECRET_KEY,
            salt=SALT,
        )
        try:
            data = serializer.loads(token)
            if data.get('code') == self.id:
                result = True
        except Exception as e:
            pass
        return result
