from pydantic import BaseModel
from entities import LoginEntity
class Login(BaseModel):
    email: str
    password: str

    def to_domain(self): 
        return LoginEntity(self.email, self.password)
