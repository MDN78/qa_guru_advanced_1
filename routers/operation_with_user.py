import random
import datetime
from models.users import UserCreatedData, UserUpdatedData
from fastapi import APIRouter, status, Response

router = APIRouter(prefix='/api', tags=['operation with users'])

now_data = datetime.datetime.now(datetime.UTC).strftime("%H:%M-%d.%m.%Y")


@router.post("/users", response_model=UserCreatedData, status_code=status.HTTP_201_CREATED)
async def create_user(name: str, job: str = 'QA') -> UserCreatedData:
    new_id = random.randint(99, 150)
    date = now_data
    return UserCreatedData(name=name, job=job, id=new_id, createdAt=date)


@router.put("/users/{user_id}", response_model=UserUpdatedData)
async def update_user(user_id: int, name: str, job: str) -> UserUpdatedData:
    users_id = [7, 8]
    date = now_data
    if user_id not in users_id:
        return Response(status_code=400, content='Uncorrect user ID')
    else:
        return UserUpdatedData(name=name, job=job, updatedAt=date)


@router.delete("/users/{user_id}")
async def delete_user():
    return Response(status_code=204)
