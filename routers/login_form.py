from models.users import User
from models.users import ResponseModel
from fastapi import HTTPException, APIRouter, Body, Response

router = APIRouter(prefix='/api', tags=['users'])


@router.get("/users/{user_id}", response_model=ResponseModel)
async def get_user(user_id: int) -> ResponseModel:
    users = {
        7: {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg",
        },
        8: {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        }
    }

    support_info = {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you.",
    }

    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return ResponseModel(data=user, support=support_info)


@router.post("/login")
def login_user(user: User = Body()):
    users = 'eve.holt@reqres.in'
    password = 'cityslicka'
    if user.email != users and user.password != password:
        return Response(status_code=400, content='Wrong email or password')

    elif user.email == users:
        return {
            "token": "QpwL5tke4Pnpja7X4"
        }
    else:
        return Response(status_code=400, content='user not found')
