from pydantic import BaseModel


class File(BaseModel):
    id: str
    name: str
    url: str



