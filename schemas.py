from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    category: str

    class Config:
        orm_config = True
