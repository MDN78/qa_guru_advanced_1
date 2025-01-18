from pydantic import BaseModel


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SupportData(BaseModel):
    url: str
    text: str


class UserCreatedData(BaseModel):
    name: str
    job: str
    id: int
    createdAt: str


class UserUpdatedData(BaseModel):
    name: str
    job: str
    updatedAt: str


class ResponseModel(BaseModel):
    data: UserData
    support: SupportData
