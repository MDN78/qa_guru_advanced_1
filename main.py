from fastapi import FastAPI
from routers import login_form

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My reqres app"}


app.include_router(login_form.router)