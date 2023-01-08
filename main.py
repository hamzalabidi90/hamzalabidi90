from fastapi import FastAPI
from modules import User, Gender, Role
from typing import List
from uuid import uuid4
app = FastAPI()

# This is a static input 
db: List[User]= [
    User(
        id= uuid4(),
        first_name="Hamza",
        last_name="Labidi",
        gender=Gender.male,
        role=[Role.admin]
    )
]

@app.get("/")
async def root():
    # no await here
    return {'Hamza': 'Labidi'} 

@app.get("/api/users")
async def show_user():
    return db

@app.post("/api/add")
async def add_user(user: User):
    db.append(user)
    return db

# we can open http://localhost:8000/docs#/ to check out api requests and history