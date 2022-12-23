from entities import LoginEntity
from db_service import Database
import jwt
import bcrypt

GET_USER_BY_EMAIL = "SELECT * FROM users WHERE email = %s"

def login_service(login: LoginEntity) -> LoginEntity:
    connection = Database.connection().cursor()
    connection.execute(GET_USER_BY_EMAIL, (login.password))
    user = connection.fetchAll()
    print(user)
    return LoginEntity()
