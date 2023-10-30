from pydantic import BaseModel
from fastapi.security import HTTPBasicCredentials
from pydantic import EmailStr

class AdminSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {"username": "hungdv@l33.dev", "password": "hungdvl33"}
        }


class AdminData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "fullname": "hungdv",
                "email": "hungdv@l33.dev",
            }
        }