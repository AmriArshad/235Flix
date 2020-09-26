from werkzeug.security import generate_password_hash, check_password_hash

from flix.adapters.repository import AbstractRepository
from flix.domain.model import User

class NameNotUniqueException(Exception):
    pass

class UnknownUserException(Exception):
    pass

class AuthenticationException(Exception):
    pass

def add_user(username: str, password: str, repo: AbstractRepository):
    # check that given username is available
    user = repo.get_user(username)
    if user is not None:
        raise NameNotUniqueException

    # if available generate password hash and store new user with hash 
    password_hash = generate_password_hash(password)

    user = User(username, password_hash)
    repo.add_user(user)

def get_user(username:str, repo: AbstractRepository):
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    return user_to_dict(user)

def authenticate_user(username: str, password: str, repo: AbstractRepository):
    authenticated = False

    user = repo.get_user(username)
    if user is not None:
        authenticated = check_password_hash(user.password, password)
    if not authenticated:
        raise AuthenticationException

def user_to_dict(user: User):
    user_dict = {
        'username': user.user_name,
        'password': user.password
    }
    return user_dict