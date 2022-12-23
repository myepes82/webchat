from pydantic import BaseModel
from typing import Optional

class Register(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    linkdin: Optional[str] = None