from fastapi import HTTPException, APIRouter
from models.users import ResponseModel

router = APIRouter(prefix='/api', tags=['users'])


@router.get("/users/{user_id}", response_model=ResponseModel)
async def get_user(user_id: int):
    # Mock data for demonstration purposes
    users = {
        7: {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg",
        }
    }

    support_info = {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you.",
    }

    user = users.get(user_id)
    if not user:
        # todo improve exception
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "data": user,
        "support": support_info,
    }



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(router, host="0.0.0.0", port=8000)


# @app.get("/api/register/{email}/{password}")
# async def get_registration_user(email: str, password: int) -> dict:
#     return {"id": 4, "token": 'QpwL5tke4Pnpja7X4',}
#
#
# @app.get("/")
# async def get_users_list() -> dict:
#     pass
