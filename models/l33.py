from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, EmailStr
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Dict

class L33_2p(Document):
    code: str
    begin_time: datetime
    open_numbers_formatted: List[str]
    issue: str
    official_time: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "code": "mb2p",
                "begin_time": "2023-10-30T00:20:00",
                "open_numbers_formatted": ['5', '3', '0', '3', '3'],
                "issue": "202310290521",
                "official_time": "2023-10-30T00:22:00"
            }
        }

    class Settings:
        name = "2p"


class UpdateL33_2pModel(BaseModel):
    code: str
    begin_time: datetime
    open_numbers_formatted: List[str]
    issue: str
    official_time: datetime

    class Collection:
        name = "2p"

    class Config:
        schema_extra = {
            "example": {
                "code": "mb2p",
                "begin_time": "2023-10-30T00:20:00",
                "open_numbers_formatted": ['5', '3', '0', '3', '3'],
                "issue": "202310290521",
                "official_time": "2023-10-30T00:22:00"
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
